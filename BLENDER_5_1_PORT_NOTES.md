# Blender 5.1 port notes

This package is a best-effort compatibility refresh of the legacy `io_object_mu` add-on.

## Changes made

- Updated `bl_info` metadata for Blender 5.1.
- Added `utils/blender_compat.py` with compatibility helpers.
- Replaced direct `mesh.use_auto_smooth = True` with a guarded compatibility call because `Mesh.use_auto_smooth` was removed in Blender 4.1+.
- Fixed temporary mesh cleanup around `Object.to_mesh()` / `to_mesh_clear()` to work more reliably with evaluated objects.
- Replaced direct `depsgraph.update()` usage with a view-layer update helper after modifier visibility changes.

## Files touched

- `__init__.py`
- `import_mu/mesh.py`
- `collider/operators.py`
- `export_mu/volume.py`
- `utils/blender_compat.py` (new)

## Caveat

This code was statically checked (`py_compile`) after the edits, but not fully runtime-tested inside a live Blender 5.1 session in this environment.
You should still test import, export, collider generation, and volume export in Blender 5.1.
