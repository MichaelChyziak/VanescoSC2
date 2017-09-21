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

import VanescoSC2.sc2Initialization
import AnalyzationAgents.analyzeBase
import logging
import signal
import sys
import glob
import random
import os
from s2clientprotocol import sc2api_pb2

def main():
    signal.signal(signal.SIGINT, signal_handler)

    logging.basicConfig(
        level=logging.DEBUG,  # Change to "level=loggin.DEBUG" to see debug messages
        format="%(levelname)-8s: %(message)s",
        datefmt="%d,%b,%Y %H:%M:%S",
        filename="log\info.log",
        filemode="w")
    logging.info("Log Start")

    sc2_socket = VanescoSC2.sc2Initialization.sc2Connection()
    replays = getReplays("C:\Users\chyziak\Desktop\my_folder\my_games\sc2\StarCraft II\Replays\Replays\\")

    saveMineralData(sc2_socket, replays)
    #readMineralData

    # #Actual network
    # (weights_first_layer, weights_second_layer) = randomizeWeights()
    #
    # replays_left = len(replays)
    # network_correct = True
    #
    # while replays_left != 0:
    #     replays_left = len(replays)
    #     for replay_name in replays:
    #         replays_left = replays_left - 1
    #         (network_correct, game_outcome) = analyzeReplay(weights_first_layer, weights_second_layer, sc2_socket, replay_name, 1)
    #         if network_correct == False:
    #             (weights_first_layer, weights_second_layer) = changeWeights(weights_first_layer, weights_second_layer, game_outcome)
    #             break
    #         (network_correct, game_outcome) = analyzeReplay(weights_first_layer, weights_second_layer, sc2_socket, replay_name, 2)
    #         if network_correct == False:
    #             (weights_first_layer, weights_second_layer) = changeWeights(weights_first_layer, weights_second_layer, game_outcome)
    #             break

def saveMineralData(sc2_socket, replays):
    replay_file = None
    if os.path.isfile("C:\Users\chyziak\Desktop\my_folder\VanescoSC2\log\mineral_info.log"):
        with open("C:\Users\chyziak\Desktop\my_folder\VanescoSC2\log\mineral_info.log", "r") as mineral_file:
            for line in mineral_file:
                if "C:\Users\chyziak\Desktop\my_folder\my_games\sc2\StarCraft II\Replays\Replays\\" in line:
                    if replay_file is None:
                        replay_file = line
                    else:
                        if replay_file == line:
                            replays.remove(replay_file)
                        replay_file = None
        mineral_file.close()

    mineral_file = open("C:\Users\chyziak\Desktop\my_folder\VanescoSC2\log\mineral_info.log", "a")

    for replay_name in replays:
        #player_id 1
        player_id = 1
        VanescoSC2.sc2Initialization.sc2ReplayStart(sc2_socket, replay_name, player_id)
        mineral_data = AnalyzationAgents.analyzeBase.analyzeMinerals(sc2_socket)
        mineral_file.write(replay_name+"\n")
        mineral_file.write(str(player_id)+"\n")
        mineral_file.write(str(mineral_data)+"\n")

        #player_id 2
        player_id = 2
        VanescoSC2.sc2Initialization.sc2ReplayStart(sc2_socket, replay_name, player_id)
        mineral_data = AnalyzationAgents.analyzeBase.analyzeMinerals(sc2_socket)
        mineral_file.write(replay_name+"\n")
        mineral_file.write(str(player_id)+"\n")
        mineral_file.write(str(mineral_data)+"\n")
    mineral_file.close()

def changeWeights(weights_first_layer, weights_second_layer, game_outcome):
    layer_size = 100

    if game_outcome == sc2api_pb2.Victory:
        for i in range(10):
            found = False
            while not found:
                rand_index = random.randint(0, (layer_size*layer_size)-1)
                if weights_first_layer[rand_index] != 1:
                    weights_first_layer[rand_index] = random.randint(weights_first_layer[rand_index] + 1, 1)
                    found = True
        for i in range(1):
            found = False
            while not found:
                rand_index = random.randint(0, layer_size-1)
                if weights_second_layer[rand_index] != 1:
                    weights_second_layer[rand_index] = random.randint(weights_second_layer[rand_index] + 1, 1)
                    found = True

    elif game_outcome == sc2api_pb2.Defeat:
        for i in range(10):
            found = False
            while not found:
                rand_index = random.randint(0, (layer_size*layer_size)-1)
                if weights_first_layer[rand_index] != -1:
                    weights_first_layer[rand_index] = random.randint(-1, weights_first_layer[rand_index] - 1)
                    found = True
        for i in range(1):
            found = False
            while not found:
                rand_index = random.randint(0, layer_size-1)
                if weights_second_layer[rand_index] != -1:
                    weights_second_layer[rand_index] = random.randint(-1, weights_second_layer[rand_index] - 1)
                    found = True

    return (weights_first_layer, weights_second_layer)

def randomizeWeights():
    random.seed(a=19)
    layer_size = 100
    weights_first_layer = [] #values 0-99 for mineral layer[0], 100-199 for mineral layer[1], etc
    weights_second_layer = [] #values 0 for first node layer[0], 1 for first node layer[1], etc

    for i in range(layer_size*layer_size):
        weights_first_layer.append(random.randint(-1, 1))
    for i in range(layer_size):
        weights_second_layer.append(random.randint(-1, 1))

    return (weights_first_layer, weights_second_layer)

def getReplays(replay_dir):
    dir_list = os.listdir(replay_dir)
    for dir_listing in dir_list:
        if ".SC2Replay" not in dir_listing:
            dir_list.remove(dir_listing)
    return dir_list


def analyzeReplay(weights_first_layer, weights_second_layer, sc2_socket, replay_name, player_id):
    network_correct = True

    VanescoSC2.sc2Initialization.sc2ReplayStart(sc2_socket, replay_name, player_id)
    (score_predictor, game_outcome) = AnalyzationAgents.analyzeBase.analyze(weights_first_layer, weights_second_layer, sc2_socket, player_id)
    if (game_outcome == sc2api_pb2.Victory and score_predictor < 0) or (game_outcome == sc2api_pb2.Defeat and score_predictor > 0):
        network_correct = False
        logging.info("Incorrect Prediction")
    else:
        logging.info("Correct Prediction")
    return (network_correct, game_outcome)

def signal_handler(signal, frame):
    log = logging.getLogger(__name__)
    log.info("Program ended using ctrl+c")
    sys.exit(0)


if __name__ == "__main__":
    main()
