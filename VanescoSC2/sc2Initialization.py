#MIT License
#
#Copyright (c) 2017 TheChyz
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from s2clientprotocol import sc2api_pb2
import sc2Command
import sc2Actions

import websocket
import subprocess
import sys
import socket
import time

import logging
log = logging.getLogger(__name__)

def sc2Connection():
    port = 5000
    args = [
        "C:\Users\chyziak\Desktop\my_folder\my_games\sc2\StarCraft II\Versions\Base55958\SC2_x64.exe", #path where SC2 x64 executable resides
        "-listen", "127.0.0.1", #listen to localhost (Blizzard recommends)
        "-port", str(port), #Blizzard recommends using port 5000
        "-displayMode", "0", #"0" means viewing in windowed mode
    ]
    log.info("Attempting to start SC2_x64.exe")
    sc2_process = subprocess.Popen(args, cwd="C:\Users\chyziak\Desktop\my_folder\my_games\sc2\StarCraft II\Support64")
    log.info("Started SC2_x64.exe")
    sc2_socket = connectSocket(port)
    log.info("Successfully connected to sc2api")
    return sc2_socket


def sc2Start(sc2_socket):
    log.info("Requesting createGame")
    sc2Command.doCommand(sc2_socket, createGame)
    log.info("Successfully requested createGame")
    log.info("Requesting joinGame")
    sc2Command.doCommand(sc2_socket, joinGame)
    log.info("Successfully requested joinGame")


def sc2Agent(sc2_socket):
    response = sc2Command.doCommand(sc2_socket, sc2Actions.action)

def sc2Observer(sc2_socket):
    for i in range(30):
        log.info("Observations #%d" % (i+1))
        response = sc2Command.doCommand(sc2_socket, getObservation)
        actions = response.observation.actions
        action_errors = response.observation.action_errors
        observation = response.observation.observation
        player_result = response.observation.player_result
        log.info("actions:\n%s" % actions)
        log.info("action_errors:\n%s" % action_errors)
        log.info("observation:\n%s" % observation)
        log.info("player_result:\n%s" % player_result)

def getObservation():
    request = sc2api_pb2.Request()
    request.observation.SetInParent()
    return request

def createGame():
    request = sc2api_pb2.Request()
    request.create_game.battlenet_map_name = "Ohana LE"
    request.create_game.realtime = True

    agent = request.create_game.player_setup.add()
    agent.type = sc2api_pb2.Participant
    agent.race = sc2api_pb2.Terran

    enemy = request.create_game.player_setup.add()
    enemy.type = sc2api_pb2.Computer
    enemy.race = sc2api_pb2.Random
    enemy.difficulty = sc2api_pb2.VeryEasy
    return request

def joinGame():
    request = sc2api_pb2.Request()
    request.join_game.options.feature_layer.width = 24 # fine tune
    request.join_game.options.feature_layer.resolution.x = 84 # fine tune
    request.join_game.options.feature_layer.resolution.y = 84 # fine tune
    request.join_game.options.feature_layer.minimap_resolution.x = 64 # fine tune
    request.join_game.options.feature_layer.minimap_resolution.y = 64 # fine tune
    request.join_game.race = sc2api_pb2.Terran
    return request


#Try to connect to the sc2api websocket for 1 minute
def connectSocket(port):
    log.info("Attempting to connect to sc2api")
    minute = 60 #number of seconds in a minute
    for i in range(minute):
        try:
            log.debug("Attempt #%d to connect to sc2api" % (i+1))
            return websocket.create_connection("ws://127.0.0.1:%s/sc2api" % port, timeout=minute)
        except socket.error:
            log.debug("Waiting 1 second before trying again")
            time.sleep(1)
    log.error("Could not connect to sc2api")
