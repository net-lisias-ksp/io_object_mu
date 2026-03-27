# vim:ts=4:et

import bpy


def clear_to_mesh(obj_eval, obj_original=None):
    """Clear temporary meshes created via Object.to_mesh() across API variants."""
    target = obj_eval if obj_eval is not None else obj_original
    if target is None:
        return
    try:
        target.to_mesh_clear()
    except RuntimeError:
        if obj_original is not None and obj_original is not target:
            try:
                obj_original.to_mesh_clear()
            except RuntimeError:
                pass


def update_view_layer(context=None):
    """Force dependency graph/view layer evaluation after modifier visibility changes."""
    if context is None:
        context = bpy.context
    try:
        context.view_layer.update()
    except AttributeError:
        pass


def enable_custom_normals(mesh):
    """Compatibility shim for split/custom normals across Blender versions.

    Blender 4.1+ removed Mesh.use_auto_smooth. Custom loop normals still work,
    so only touch the property when it exists.
    """
    if hasattr(mesh, "use_auto_smooth"):
        mesh.use_auto_smooth = True
