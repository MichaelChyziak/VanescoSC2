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
    (weights_first_layer, weights_second_layer) = randomizeWeights()

    replays_left = len(replays)
    network_correct = True

    while replays_left != 0:
        replays_left = len(replays)
        for replay_name in replays:
            replays_left = replays_left - 1
            network_correct = analyzeReplay(weights_first_layer, weights_second_layer, sc2_socket, replay_name, 1)
            if network_correct == False:
                (weights_first_layer, weights_second_layer) = changeWeights(weights_first_layer, weights_second_layer)
                break
            network_correct = analyzeReplay(weights_first_layer, weights_second_layer, sc2_socket, replay_name, 2)
            if network_correct == False:
                (weights_first_layer, weights_second_layer) = changeWeights(weights_first_layer, weights_second_layer)
                break

def changeWeights(weights_first_layer, weights_second_layer):
    layer_size = 100

    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)
    weights_first_layer[random.randint(0, (layer_size*layer_size)-1)] = random.randint(-1, 1)

    weights_second_layer[random.randint(0, layer_size-1)] = random.randint(-1, 1)

    return (weights_first_layer, weights_second_layer)

def randomizeWeights():
    random.seed(a=1)
    layer_size = 100
    weights_first_layer = [] #values 0-99 for mineral layer[0], 100-199 for mineral layer[1], etc
    weights_second_layer = [] #values 0 for first node layer[0], 1 for first node layer[1], etc

    for i in range(layer_size*layer_size):
        weights_first_layer.append(random.randint(-1, 1))
    for i in range(layer_size):
        weights_second_layer.append(random.randint(-1, 1))

    return (weights_first_layer, weights_second_layer)

def getReplays(replay_dir):
    return glob.glob(replay_dir+"*.SC2Replay")


def analyzeReplay(weights_first_layer, weights_second_layer, sc2_socket, replay_name, player_id):
    network_correct = True

    VanescoSC2.sc2Initialization.sc2ReplayStart(sc2_socket, replay_name, player_id)
    (score_predictor, game_outcome) = AnalyzationAgents.analyzeBase.analyze(weights_first_layer, weights_second_layer, sc2_socket, player_id)
    if (game_outcome == sc2api_pb2.Victory and score_predictor < 0) or (game_outcome == sc2api_pb2.Defeat and score_predictor > 0):
        network_correct = False
        logging.info("Incorrect Prediction")
    else:
        logging.info("Correct Prediction")
    return network_correct

def signal_handler(signal, frame):
    log = logging.getLogger(__name__)
    log.info("Program ended using ctrl+c")
    sys.exit(0)


if __name__ == "__main__":
    main()
