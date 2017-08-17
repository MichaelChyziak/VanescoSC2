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

from s2clientprotocol import sc2api_pb2, spatial_pb2, ui_pb2

import random
import time
import VanescoSC2.sc2Actions
import VanescoSC2.sc2Command
import VanescoSC2.sc2Initialization

import logging
log = logging.getLogger(__name__)

def run(sc2_socket):
    random.seed(a=1)
    while True:
        (observation, data, query) = VanescoSC2.sc2Initialization.sc2Observer(sc2_socket)
        #
        # rand_x = random.randint(0, 64)
        # rand_y = random.randint(0, 64)
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.moveCamera, rand_x, rand_y)
        #
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.chat,
        #                                             You are playing against VanescoSC2, a Starcaft 2 AI")
        #
        # rand_x_start = random.randint(0, 84)
        # rand_y_start = random.randint(0, 84)
        # rand_x_end = random.randint(0, 84)
        # rand_y_end = random.randint(0, 84)
        # rand_add = bool(random.getrandbits(1))
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.unitSelectScreenArea,
        #                                                 rand_x_start, rand_y_start, rand_x_end, rand_y_end, rand_add)
        #
        # rand_x = random.randint(0, 84)
        # rand_y = random.randint(0, 84)
        # rand_type = random.choice([spatial_pb2.ActionSpatialUnitSelectionPoint.Select,
        #                             spatial_pb2.ActionSpatialUnitSelectionPoint.Toggle,
        #                             spatial_pb2.ActionSpatialUnitSelectionPoint.AllType,
        #                             spatial_pb2.ActionSpatialUnitSelectionPoint.AddAllType])
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.unitSelectPoint,
        #                                             rand_x, rand_y, rand_type)
        #
        # ability_list = getAbilitiesForUnit(observation)
        # if ability_list: #makes sure that ability_list is not empty
        #   rand_ability_id = random.choice(ability_list)
        #   rand_x = rand_y = random.randint(0, 84)
        #   rand_y = rand_y = random.randint(0, 84)
        #   rand_queue_command = bool(random.getrandbits(1))
        #   response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.unitCommandScreen,
        #                                               rand_ability_id, rand_x, rand_y, rand_queue_command)
        #
        #
        # ability_list = getAbilitiesForUnit(observation)
        # if ability_list: #makes sure that ability_list is not empty
        #   rand_ability_id = random.choice(ability_list)
        #   rand_x = rand_y = random.randint(0, 84)
        #   rand_y = rand_y = random.randint(0, 84)
        #   rand_queue_command = bool(random.getrandbits(1))
        #   response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.unitCommandMinimap,
        #                                               rand_ability_id, rand_x, rand_y, rand_queue_command)
        #
        #
        # rand_action = random.choice([ui_pb2.ActionControlGroup.Recall,
        #                             ui_pb2.ActionControlGroup.Set,
        #                             ui_pb2.ActionControlGroup.Append,
        #                             ui_pb2.ActionControlGroup.SetAndSteal,
        #                             ui_pb2.ActionControlGroup.AppendAndSteal])
        # rand_index = random.randint(0, 9)
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.controlGroupRecall,
        #                                             rand_action, rand_index)
        #
        #
        # rand_add = bool(random.getrandbits(1))
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.selectArmy, rand_add)
        #
        #
        #
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.selectLarva)
        #
        #
        #
        # rand_click_type = random.choice([ui_pb2.ActionSelectIdleWorker.Set,
        #                             ui_pb2.ActionSelectIdleWorker.Add,
        #                             ui_pb2.ActionSelectIdleWorker.All,
        #                             ui_pb2.ActionSelectIdleWorker.AddAll])
        # response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.selectIdleWorker,
        #                                             rand_click_type)
        #
        #
        #

# observation.observation.observation.abilities is repeated
# observation.observation.observation.abilities.ability_id has the possible list of ability_id that can be taken
# observation should be a observation
# This function will return a list of possible ability_id if possible, otherwise it will return an empty list
def getAbilitiesForUnit(observation):
    ability_id_list = []
    for ability in observation.observation.observation.abilities:
        ability_id_list.append(ability.ability_id)
    return ability_id_list
