#!/usr/bin/env python

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

import random
import time
import VanescoSC2.sc2Actions
import VanescoSC2.sc2Command
import VanescoSC2.sc2Initialization

import logging
log = logging.getLogger(__name__)

global_minerals = [50]
global_game_loop = [0]


def run(sc2_socket):
    random.seed(a=1)
    while True:
        time.sleep(1)
        (observation, data, query) = VanescoSC2.sc2Initialization.sc2Observer(sc2_socket)
        minerals = observation.observation.observation.player_common.minerals
        game_loop = observation.observation.observation.game_loop
        print(calculateMineralsPerMinute(minerals, game_loop))
        rand_x = random.randint(0, 64)
        rand_y = random.randint(0, 64)
        response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.moveCamera, rand_x, rand_y)

# Calculates mineral income per minute
# Updates values based on 10 second intervals
def calculateMineralsPerMinute(minerals, game_loop):
    game_loops_per_min = 1344 # 22.4 gameloops/s From Blizzard * 60s/min
    game_loops_per_interval = 22.4 * 10
    min_per_game_loop = 1.0/float(game_loops_per_min)
    if (game_loop - global_game_loop[0]) > game_loops_per_interval:
        global_minerals.pop(0)
        global_game_loop.pop(0)
    global_minerals.append(minerals)
    global_game_loop.append(game_loop)
    delta_minerals = global_minerals[len(global_minerals)-1] - global_minerals[0]
    delta_game_loop = global_game_loop[len(global_game_loop)-1] - global_game_loop[0]
    return float(delta_minerals)/float(delta_game_loop*min_per_game_loop)
