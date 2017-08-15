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

def action():
    request = chat("Hello");
    return request

# Values of x and y must be from (and including) 0-64
# Simulates click on minimap
def moveCamera(x, y):
    log.debug("Moving Camera:\nx-axis=%d\ny-axis=%d" % (x, y))
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action.action_feature_layer.camera_move.center_minimap.x = x
    action.action_feature_layer.camera_move.center_minimap.y = y
    return request

# Sends a message to "all chat"
# TODO not working
# message ActionChat {
#   enum Channel {
#     Broadcast = 1;
#     Team = 2;
#   }
#   optional Channel channel = 1;
#   optional string message = 2;
# }
def chat(message):
    request = sc2api_pb2.Request()
    action = request.action.actions.add()
    action = action.chat.add()
    action.channel = sc2api_pb2.ActionChat.Broadcast
    action.message = message
    return request



# message RequestAction {
#    repeated Action actions = 1;
# }
#
# message Action {
#   optional ActionSpatial action_feature_layer = 2;          // Populated if Feature Layer interface is enabled.
#   optional ActionUI action_ui = 4;                          // Populated if Feature Layer or Render interface is enabled.
#   repeated ActionChat chat = 5;                             // Chat messages as a player typing into the chat channel.
# }
#
#
#
#
#
# message ActionSpatial {
#   oneof action {
#     ActionSpatialUnitCommand unit_command = 1;
#     ActionSpatialCameraMove camera_move = 2;
#     ActionSpatialUnitSelectionPoint unit_selection_point = 3;
#     ActionSpatialUnitSelectionRect unit_selection_rect = 4;
#   }
# }
#
# message ActionSpatialUnitCommand {
#   optional int32 ability_id = 1;
#   oneof target {
#     PointI target_screen_coord = 2;
#     PointI target_minimap_coord = 3;
#   }
#
#   optional bool queue_command = 4;          // Equivalent to shift+command.
# }
#
# message ActionSpatialCameraMove {
#   optional PointI center_minimap = 1;       // Simulates a click on the minimap to move the camera.
# }
#
# message ActionSpatialUnitSelectionPoint {
#   optional PointI selection_screen_coord = 1;
#   enum Type {
#     Select = 1;         // Equivalent to normal click. Changes selection to unit.
#     Toggle = 2;         // Equivalent to shift+click. Toggle selection of unit.
#     AllType = 3;        // Equivalent to control+click. Selects all units of a given type.
#     AddAllType = 4;     // Equivalent to shift+control+click. Selects all units of a given type.
#   }
#   optional Type type = 2;
# }
#
# message ActionSpatialUnitSelectionRect {
#   repeated RectangleI selection_screen_coord = 1;   // Eventually this should not be an array, but a single field (multiple would be cheating).
#   optional bool selection_add = 2;                  // Equivalent to shift+drag. Adds units to selection.
# }
#
# // Point on the screen/minimap (e.g., 0..64).
# // Note: bottom left of the screen is 0, 0.
# message PointI {
#   optional int32 x = 1;
#   optional int32 y = 2;
# }
#
# // Screen space rectangular area.
# message RectangleI {
#   optional PointI p0 = 1;
#   optional PointI p1 = 2;
# }
#
#
#
#
#
#
#
#
#
# message ActionUI {
#   oneof action {
#     ActionControlGroup control_group = 1;
#     ActionSelectArmy select_army = 2;
#     ActionSelectWarpGates select_warp_gates = 3;
#     ActionSelectLarva select_larva = 4;
#     ActionSelectIdleWorker select_idle_worker = 5;
#     ActionMultiPanel multi_panel = 6;
#     ActionCargoPanelUnload cargo_panel = 7;
#     ActionProductionPanelRemoveFromQueue production_panel = 8;
#     ActionToggleAutocast toggle_autocast = 9;
#   }
# }
#
# message ActionControlGroup {
#   enum ControlGroupAction {
#     Recall = 1;             // Equivalent to number hotkey. Replaces current selection with control group.
#     Set = 2;                // Equivalent to Control + number hotkey. Sets control group to current selection.
#     Append = 3;             // Equivalent to Shift + number hotkey. Adds current selection into control group.
#     SetAndSteal = 4;        // Equivalent to Control + Alt + number hotkey. Sets control group to current selection. Units are removed from other control groups.
#     AppendAndSteal = 5;     // Equivalent to Shift + Alt + number hotkey. Adds current selection into control group. Units are removed from other control groups.
#   }
#   optional ControlGroupAction action = 1;
#   optional uint32 control_group_index = 2;
# }
#
# message ActionSelectArmy {
#   optional bool selection_add = 1;
# }
#
# message ActionSelectWarpGates {
#   optional bool selection_add = 1;
# }
#
# message ActionSelectLarva {
# }
#
# message ActionSelectIdleWorker {
#   enum Type {
#     Set = 1;        // Equivalent to click with no modifiers. Replaces selection with single idle worker.
#     Add = 2;        // Equivalent to shift+click. Adds single idle worker to current selection.
#     All = 3;        // Equivalent to control+click. Selects all idle workers.
#     AddAll = 4;     // Equivalent to shift+control+click. Adds all idle workers to current selection.
#   }
#   optional Type type = 1;
# }
#
# message ActionMultiPanel {
#   enum Type {
#     SingleSelect = 1;         // Click on icon
#     DeselectUnit = 2;         // Shift Click on icon
#     SelectAllOfType = 3;      // Control Click on icon.
#     DeselectAllOfType = 4;    // Control+Shift Click on icon.
#   }
#   optional Type type = 1;
#   optional int32 unit_index = 2;
# }
#
# message ActionCargoPanelUnload {
#   optional int32 unit_index = 1;
# }
#
# message ActionProductionPanelRemoveFromQueue {
#   optional int32 unit_index = 1;
# }
#
# message ActionToggleAutocast {
#   optional int32 ability_id = 1;
# }
