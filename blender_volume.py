import bpy
import bmesh

def calculate_volume(obj):
    if obj.type != 'MESH':
        print(f"Selected object {obj.name} is not a mesh.")
        return

    # Duplicate and apply modifiers
    temp_obj = obj.copy()
    temp_obj.data = obj.data.copy()
    bpy.context.collection.objects.link(temp_obj)
    bpy.context.view_layer.objects.active = temp_obj

    bpy.ops.object.select_all(action='DESELECT')
    temp_obj.select_set(True)

    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.transform_apply(scale=True)

    # Calculate volume
    mesh = temp_obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    volume = bm.calc_volume(signed=False)
    bm.free()

    # Cleanup
    bpy.data.objects.remove(temp_obj)

    print(f"Volume of {obj.name}: {volume:.6f} cubic Blender units")

# Run for active object
obj = bpy.context.active_object
if obj:
    calculate_volume(obj)
else:
    print("No active object selected.")
