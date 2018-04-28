# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# todo:
# - automation for switching assets
# --- sombrero -> sombrero 278
# --- pointy -> pointy blocking 278
# -- read unwanted proxy for action, create new proxy and apply new action

bl_info = {
    "name": "Blockout Helper",
    "author": "QUOLLISM",
    "version": (0,1),
    "blender": (2, 77, 0),
    "description": "Extra buttons to help with layout and blocking",
    "category": "Animation" }

import bpy

def view3d_extra_buttons(self, context):
    row = self.layout.row(align=True)
    row.prop(context.space_data, "show_only_render", text="Boomsmash", icon='RENDER_ANIMATION')
    row.prop(context.space_data, "show_background_images", text="BG", icon='FILE_IMAGE')

def timeline_extra_buttons(self, context):
    layout = self.layout
    layout.prop(context.user_preferences.edit, "keyframe_new_interpolation_type", text="", icon_only=True)

def register():
    bpy.types.VIEW3D_HT_header.append(view3d_extra_buttons)
    bpy.types.TIME_HT_header.append(timeline_extra_buttons)
    # register replacer operator

def unregister():
    bpy.types.VIEW3D_HT_header.remove(view3d_extra_buttons)
    bpy.types.TIME_HT_header.remove(timeline_extra_buttons)

if __name__ == "__main__":
    register()
