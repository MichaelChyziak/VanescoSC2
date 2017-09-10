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

import struct

import numpy

import logging
log = logging.getLogger(__name__)

def run(request):
    player_common = request.observation.observation.player_common
    feature_layer_data = request.observation.observation.feature_layer_data
    game_loop = request.observation.observation.game_loop

    #TODO Add these also?
    #alerts
    #abilities
    #score
    #ui_data

    # Input features
    minerals = player_common.minerals
    # vespene = player_common.minerals
    # food_cap = player_common.food_cap
    # food_used = player_common.food_used
    # food_army = player_common.food_army
    # food_workers = player_common.food_workers
    # idle_worker_count = player_common.idle_worker_count
    # army_count = player_common.army_count
    # warp_gate_count = player_common.warp_gate_count
    #
    # #TODO change to matrices
    # screen_height_map = numpy.fromstring(feature_layer_data.renders.height_map.data, dtype=numpy.uint8).tolist()
    # screen_visibility_map = numpy.fromstring(feature_layer_data.renders.visibility_map.data, dtype=numpy.uint8).tolist()
    # screen_creep = numpy.unpackbits(numpy.fromstring(feature_layer_data.renders.creep.data, dtype=numpy.uint8)).tolist()
    # screen_power = numpy.unpackbits(numpy.fromstring(feature_layer_data.renders.power.data, dtype=numpy.uint8)).tolist()
    # screen_player_id = numpy.fromstring(feature_layer_data.renders.player_id.data, dtype=numpy.uint8).tolist()
    # screen_unit_type = numpy.fromstring(feature_layer_data.renders.unit_type.data, dtype=numpy.int32).tolist()
    # screen_selected = numpy.unpackbits(numpy.fromstring(feature_layer_data.renders.selected.data, dtype=numpy.uint8)).tolist()
    # screen_unit_hit_points = numpy.fromstring(feature_layer_data.renders.unit_hit_points.data, dtype=numpy.int32).tolist()
    # screen_unit_hit_points_ratio = numpy.fromstring(feature_layer_data.renders.unit_hit_points_ratio.data, dtype=numpy.uint8).tolist()
    # screen_unit_energy = numpy.fromstring(feature_layer_data.renders.unit_energy.data, dtype=numpy.int32).tolist()
    # screen_unit_shields = numpy.fromstring(feature_layer_data.renders.unit_shields.data, dtype=numpy.int32).tolist()
    # screen_unit_density_aa = numpy.fromstring(feature_layer_data.renders.unit_density_aa.data, dtype=numpy.uint8).tolist()
    # screen_unit_density = numpy.fromstring(feature_layer_data.renders.unit_density.data, dtype=numpy.uint8).tolist()
    #
    # minimap_height_map = numpy.fromstring(feature_layer_data.minimap_renders.height_map.data, dtype=numpy.uint8).tolist()
    # minimap_visibility_map = numpy.fromstring(feature_layer_data.minimap_renders.visibility_map.data, dtype=numpy.uint8).tolist()
    # minimap_creep = numpy.unpackbits(numpy.fromstring(feature_layer_data.minimap_renders.creep.data, dtype=numpy.uint8)).tolist()
    # minimap_camera = numpy.unpackbits(numpy.fromstring(feature_layer_data.minimap_renders.camera.data, dtype=numpy.uint8)).tolist()
    # minimap_player_id = numpy.fromstring(feature_layer_data.minimap_renders.player_id.data, dtype=numpy.uint8).tolist()
    # minimap_selected = numpy.unpackbits(numpy.fromstring(feature_layer_data.minimap_renders.selected.data, dtype=numpy.uint8)).tolist()
    # minimap_unit_type = numpy.fromstring(feature_layer_data.minimap_renders.unit_type.data, dtype=numpy.int32).tolist()
    #
    # info_string = ( "Current Game Stats -->\nScore predictor: %d\nMinerals: %d\nVespene: %d\nFood cap: %d\n"
    #                 "Food used: %d\nFood army: %d\nFood workers: %d\nIdle worker count: %d\nArmy count: %d\n"
    #                 "Warp gate count: %d\nScreen height map: %s\nScreen visibility map: %s\nScreen creep: %s\n"
    #                 "Screen power: %s\nScreen player id: %s\nScreen unit type: %s\nScreen selected: %s\n"
    #                 "Screen unit hit points: %s\nScreen unit energy: %s\nScreen unit shields: %s\n"
    #                 "Screen unit density aa: %s\nScreen unit density: %s\nScreen unit hit points ratio: %s\n"
    #                 "Minimap height map: %s\nMinimap visibility map: %s\nMinimap creep: %s\nMinimap camera: %s\n"
    #                 "Minimap player id: %s\nMinimap selected: %s\nMinimap unit type: %s\nGame loop: %s\n" %
    #                 (score_predictor, minerals, vespene, food_cap, food_used, food_army, food_workers, idle_worker_count,
    #                 army_count, warp_gate_count, screen_height_map, screen_visibility_map, screen_creep, screen_power,
    #                 screen_player_id, screen_unit_type, screen_selected, screen_unit_hit_points, screen_unit_energy,
    #                 screen_unit_shields, screen_unit_density_aa, screen_unit_density, screen_unit_hit_points_ratio,
    #                 minimap_height_map, minimap_visibility_map, minimap_creep, minimap_camera,
    #                 minimap_player_id, minimap_selected, minimap_unit_type, game_loop))
    #
    # log.info(info_string)

    return (minerals, game_loop)
