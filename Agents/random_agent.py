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
        request = VanescoSC2.sc2Initialization.sc2Observer(sc2_socket)
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
        # ability_list = getAbilitiesForUnit(request)
        # if ability_list: #makes sure that ability_list is not empty
        #   rand_ability_id = random.choice(ability_list)
        #   rand_x = rand_y = random.randint(0, 84)
        #   rand_y = rand_y = random.randint(0, 84)
        #   rand_queue_command = bool(random.getrandbits(1))
        #   response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.unitCommandScreen,
        #                                               rand_ability_id, rand_x, rand_y, rand_queue_command)
        #
        #
        # ability_list = getAbilitiesForUnit(request)
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
        # units_selected = getUnitsSelected(request)
        # if units_selected:
        #     rand_unit_index = random.randint(1, len(units_selected))
        #     rand_panel_type = random.choice([ui_pb2.ActionMultiPanel.SingleSelect,
        #                                       ui_pb2.ActionMultiPanel.DeselectUnit,
        #                                       ui_pb2.ActionMultiPanel.SelectAllOfType,
        #                                       ui_pb2.ActionMultiPanel.DeselectAllOfType])
        #     response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.multiPanel,
        #                                                  rand_panel_type, rand_unit_index)
        #
        #
        #
        # units_cargo = getUnitsCargo(request)
        # if units_cargo:
        #     rand_unit_index = random.randint(0, len(units_cargo))
        #     response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.cargoPanel,
        #                                                  rand_unit_index)
        #
        #
        #
        # units_queued = getUnitsQueued(request)
        # if units_queued:
        #     rand_unit_index = random.randint(0, len(units_queued))
        #     response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.productionPanel,
        #                                                  rand_unit_index)
        #
        #
        #
        # ability_list = getAbilitiesForUnit(request)
        # if ability_list: #makes sure that ability_list is not empty
        #   rand_ability_id = random.choice(ability_list)
        #   response = VanescoSC2.sc2Command.doCommand(sc2_socket, VanescoSC2.sc2Actions.toggleAutocast,
        #                                               rand_ability_id)


# This function will return a list of possible ability_id if possible, otherwise it will return an empty list
def getAbilitiesForUnit(request):
    ability_id_list = []
    for ability in request.observation.observation.abilities:
        ability_id_list.append(ability.ability_id)
    return ability_id_list

# This function will return a list of all of the units that can be selected. If none will return an empty list
def getUnitsSelected(request):
    units_selected = []
    for unit in request.observation.observation.ui_data.single.unit:
        if unit.player_relative == 1:
            units_selected.append(unit.unit_type)
    for units in request.observation.observation.ui_data.multi.unit:
        if units.player_relative == 1:
            units_selected.append(units.unit_type)

# Return a list of all of the units in a cargo (including the cargo itself). If none will return an empty list
# TODO untested
def getUnitsCargo(request):
    for unit in request.observation.observation.ui_data.cargo.unit:
        if unit.player_relative == 1:
            units_selected.append(unit.unit_type)
            for cargo in unit.passengers:
                units_selected.append(cargo.unit_type)

# Return a list of all of the units in a queued (including the original). If none will return an empty list
# TODO untested
def getUnitsQueued(request):
    for unit in request.observation.observation.ui_data.production.unit:
        if unit.player_relative == 1:
            units_selected.append(unit.unit_type)
            for queue in unit.build_queue:
                units_selected.append(queue.unit_type)
