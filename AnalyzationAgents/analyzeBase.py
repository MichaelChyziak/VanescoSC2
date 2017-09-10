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
import VanescoSC2.sc2Command
import AnalyzationAgents.agent
from s2clientprotocol import sc2api_pb2

import logging
log = logging.getLogger(__name__)

def analyze(weights_first_layer, weights_second_layer, sc2_socket, player_id):

    # Output (positive # = win, negative # = loss)
    score_predictor = 0
    layer_size = 100
    mineral_step_loop = 0
    mineral_layer = [0] * layer_size

    nodes_first_layer = [0] * layer_size
    final_node = 0


    game_done = False
    game_outcome = None
    while not game_done:
        observation = VanescoSC2.sc2Initialization.sc2Observer(sc2_socket)
        if observation.observation.player_result:
            game_outcome = observation.observation.player_result[player_id-1].result
            game_done = True

        (mineral_value, game_loop) = AnalyzationAgents.agent.run(observation)
        VanescoSC2.sc2Command.doCommand(sc2_socket, stepReplay)

        #Add new value to layer
        mineral_layer= [mineral_value] + mineral_layer[0:(layer_size-1)]

        #Calculate first node value layer
        for i in range(layer_size):
            nodes_first_layer[i] = (mineral_layer[0] * weights_first_layer[i*layer_size])
            for j in range(1, layer_size):
                nodes_first_layer[i] = nodes_first_layer[i] + (mineral_layer[j] * weights_first_layer[(i*layer_size) + j])

        final_node = 0
        for i in range(layer_size):
            final_node = final_node + (nodes_first_layer[i] * weights_second_layer[i])

        score_predictor = score_predictor + final_node

        #log.info("Game Loop: %d" % game_loop)
        #log.info("Final Node: %d" % final_node)
        #log.info("Score Predictor: %d" % score_predictor)
    log.info("Game Complete")
    log.info("Weights First Layer: "+str(weights_first_layer))
    log.info("Weights Second Layer: "+str(weights_second_layer))
    log.info("Score Predictor: %d" % score_predictor)
    return (score_predictor, game_outcome)

def stepReplay():
    request = sc2api_pb2.Request()
    request.step.count = 1
    return request
