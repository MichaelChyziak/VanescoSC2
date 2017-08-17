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

import logging
log = logging.getLogger(__name__)

# Values of x and y must be from (and including) 0-64
# Simulates click on minimap
def moveCamera(x, y):
    # log.debug("Moving Camera:\nx-axis=%d\ny-axis=%d" % (x, y))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_feature_layer.camera_move.center_minimap.x = x
    action.action_feature_layer.camera_move.center_minimap.y = y
    #print(request.ListFields()) #For debugging
    return request

# Sends a message to "all chat"
# TODO Response returns "Error"
# message ActionChat {
#   enum Channel {
#     Broadcast = 1;
#     Team = 2;
#   }
#   optional Channel channel = 1;
#   optional string message = 2;
# }
def chat(message):
    # log.debug("Sending message to all chat:\n%s" % message)
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action_chat = action.chat.add()
    action_chat.message = message
    action_chat.channel = sc2api_pb2.ActionChat.Broadcast
    #print(request.ListFields()) #For debugging
    return request

# Selects units in a rectangle on the screen
# Can also add units to the selection
# resolutions of x and y come from "request.join_game.options.feature_layer"
# x_start: 0-84
# y_start: 0-84
# x_end: 0-84
# y_end: 0-84
# add: bool value; if the area selected should add the units highlighted to the current selection
def unitSelectScreenArea(x_start, y_start, x_end, y_end, add):
    # log.debug("Selecting Screen Area:\nx_start=%d\ny_start=%d\nx_end=%d\ny_end=%d\nadd=%r" %
    #             (x_start, y_start, x_end, y_end, add))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    screen_selection = action.action_feature_layer.unit_selection_rect.selection_screen_coord.add()
    screen_selection.p0.x = x_start
    screen_selection.p0.y = y_start
    screen_selection.p1.x = x_end
    screen_selection.p1.y = y_end
    action.action_feature_layer.unit_selection_rect.selection_add = add
    return request

# Selects a unit at a point on the screen
# resolutions of x and y come from "request.join_game.options.feature_layer"
# x: 0-84
# y: 0-84
# click_type: one of the following (all starting with "spatial_pb2.ActionSpatialUnitSelectionPoint")
#               .Select (normal click. Changes selection to unit.)
#               .Toggle (shift+click. Toggle selection of unit)
#               .AllType (control+click. Selects all units of a given type.)
#               .AddAllType (shift+control+click. Selects all units of a given type.)
# TODO response sometimes gives error, but that may be due to not having anything clickable at that location
# TODO seems to work, should debug further to make sure tho
def unitSelectPoint(x, y, click_type):
    # log.debug("Selecting Point:\nx=%d\ny=%d\nclick_type=%d" % (x, y, click_type))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_feature_layer.unit_selection_point.selection_screen_coord.x = x
    action.action_feature_layer.unit_selection_point.selection_screen_coord.y = y
    action.action_feature_layer.unit_selection_point.type = click_type
    return request



# Send a command to a unit on the screen
# resolutions of x and y come from "request.join_game.options.feature_layer"
# ability_id: The number of the ability_id
# x: 0-84
# y: 0-84
# queue_command: bool (like a shift command to be peformed, queued)
def unitCommandScreen(ability_id, x, y, queue_command):
    # log.debug("Unit Command Screen:\nability_id=%d\nx=%d\ny=%d\queue_command=%r"
    #             % (ability_id, x, y, queue_command))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_feature_layer.unit_command.ability_id = ability_id
    action.action_feature_layer.unit_command.target_screen_coord.x = x
    action.action_feature_layer.unit_command.target_screen_coord.y = y
    action.action_feature_layer.unit_command.queue_command = queue_command
    return request

# Send a command to a unit on the minimap
# resolutions of x and y come from "request.join_game.options.feature_layer"
# ability_id: The number of the ability_id
# x: 0-64
# y: 0-64
# queue_command: bool (like a shift command to be peformed, queued)
def unitCommandMinimap(ability_id, x, y, queue_command):
    # log.debug("Unit Command Screen:\nability_id=%d\nx=%d\ny=%d\queue_command=%r"
    #             % (ability_id, x, y, queue_command))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_feature_layer.unit_command.ability_id = ability_id
    action.action_feature_layer.unit_command.target_minimap_coord.x = x
    action.action_feature_layer.unit_command.target_minimap_coord.y = y
    action.action_feature_layer.unit_command.queue_command = queue_command
    return request


# Equivalent to number hotkey. Replaces current selection with control group.
# action_input: one of the following (all starting with "ui_pb2.ActionControlGroup")
#               .Recall (number hotkey. Replaces current selection with control group.)
#               .Set (Control + number hotkey. Sets control group to current selection.)
#               .Append (Shift + number hotkey. Adds current selection into control group.)
#               .SetAndSteal (Control + Alt + number hotkey. Sets control group to current selection.
#                              Units are removed from other control groups.
#               .AppendAndSteal (Shift + Alt + number hotkey. Adds current selection into control group.
#                               Units are removed from other control groups.)
# control_group_index: TODO find out what this is exactly, is this keyboard values 0-9? (I guessed it is atm)
def controlGroupRecall(action_input, index):
    # log.debug("Control Group Recall:\naction=%d\nindex=%d" % (action, index))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.control_group.action = action_input
    action.action_ui.control_group.control_group_index = index
    return request


# Select army hotkey
# add: bool value. add army to current selection?
def selectArmy(add):
    # log.debug("Select Army:\nadd=%r" % (add))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.select_army.selection_add = add
    return request

# Select warp gates hotkey
# add: bool value. add warp gates to current selection?
def selectWarpGates(add):
    # log.debug("Select Warp Gates:\nadd=%r" % (add))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.select_warp_gates.selection_add = add
    return request

# Select larva
# Works but only on hatcher/lair/hive
def selectLarva():
    # log.debug("Select Larva")
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.select_larva.SetInParent()
    return request

# Select idle worker(s)
# click_type: one of the following (all starting with "ui_pb2.ActionSelectIdleWorker")
#               .Set (click with no modifiers. Replaces selection with single idle worker.)
#               .Add (shift+click. Adds single idle worker to current selection.)
#               .All (control+click. Selects all idle workers.)
#               .AddAll (shift+control+click. Adds all idle workers to current selection.)
def selectIdleWorker(click_type):
    # log.debug("Select Idle Worker:\nclick_type=%d" % (click_type))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.select_idle_worker.type = click_type
    return request


# Click on icons?
# panel_type: one of the following (all starting with "ui_pb2.ActionMultiPanel")
#               .SingleSelect (Click on icon)
#               .DeselectUnit (Shift Click on icon)
#               .SelectAllOfType (Control Click on icon.)
#               .DeselectAllOfType (Control+Shift Click on icon.)
# Select a specific unit from the multi-unit selection
# TODO test out
def multiPanel(panel_type, unit_index):
    # log.debug("Multi Panel:\ntype=%d\nunit_index=%d" % (panel_type, unit_index))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.multi_panel.type = panel_type
    action.action_ui.multi_panel.unit_index = unit_index
    return request

# Not sure what this is...
# TODO untested
def cargoPanel(unit_index):
    # log.debug("Cargo Panel:\nunit_index=%d" % (unit_index))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.cargo_panel.unit_index = unit_index
    return request

# Not sure what this is...
# TODO untested
def productionPanel(unit_index):
    # log.debug("Production Panel:\nunit_index=%d" % (unit_index))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.production_panel.unit_index = unit_index
    return request

# Toggle autocast on an ability
# TODO untested
def toggleAutocast(ability_id):
    # log.debug("Toggle Autocast:\nability_id=%d" % (ability_id))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_ui.toggle_autocast.ability_id = ability_id
    return request
