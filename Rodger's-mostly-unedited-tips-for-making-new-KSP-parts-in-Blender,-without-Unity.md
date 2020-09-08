In the same directory as your .blend, create a new .cfg file for your part, and add `.in` to the end of the file name (partname.cfg.in). There is a template included in the addon which includes calculations for volume/mass based on the mesh, but you can also just copy a stock cfg to start with.

Once the cfg.in file is in the directory, when you export the part, the exporter will add certain things to a new cfg file it'll create based on the cfg.in:
Empty objects called `node_XXX` will be turned into NODE{} definitions (single arrow helps see their rotation, but empty type doesnt matter). For surface attachment nodes, call the empty `node_attach`, and the exporter will add a "regular" node definition with the location data in it, as NODE{} doesn't work for srf attachment.
The location of empty objects called CoMOffset, CoPOffset, or CoLOffset will be used to set CoM/CoP/CoL.

Make sure your cfg.in has `rescaleFactor = 1.0` and `scale = 1.0`. Otherwise KSP defaults to a 1.25 scale, so a 1m part in blender will come out as a 1.25m part in KSP.

Create an empty as the "root" part for your part, and name it the same as your part.cfg.in file (without the `.cfg.in` extensions). Child your meshes, colliders, and other transforms(empties) to this (shift drag the objects on top of the root empty is one way to do this). Make sure your meshes have their transforms applied (crtl A), so the transform panel reads 0° for the rotations, and 1.0 for the scale. Then select the root object, press `clearInverse`, double check nothing's out of place (colliders will move if you moved them originally via transform panel), then press the `export mu model` button. It will create a .mu file with the name of the root part, and a .cfg file too.

If something's out of place in-game, selecting the root object, and pressing the `clearInverse` button and then re-exporting will most likely fix it.

The exporter will strip all ".xxx" suffixes, so you can have multiple instances of the same name in KSP, even when blender adds the numbered suffix to differentiate different instances with the same name.

Add colliders via `add mu collider` tab inside the tool menu, or button at top. adjust size on creation, or in Mu Collider panel to adjust colliders size/location, inside the object properties panel of the properties editor, not the blender transform location/scale. Rotation needs to be done with blender's transform panel, but doesn't seem to cause any issues (and you seem to be able to get away with translations too). The `isTrigger` option makes a non-solid collider, for ladders/hatches etc. (you can use Sarbian's DebugStuff to view colliders in-game - https://forum.kerbalspaceprogram.com/index.php?/topic/135726-18-debugstuff-2019-10-22-see-the-hidden-secrets-of-the-game-objects/)

In the Mu Shader panel, select the KSP shader you want to use for the part (the dropdown menu should have entries like "KSP Diffuse", "KSP Bumped Specular" etc), then in the textures tab, Name: `_MainTex`, under that change 'grey' to your diffuse texture name. same for different maps eg `_BumpMap` (from `bump` to your normal map) or `_Emissive` (from `white`)

For flag objects, go to the Mu Properties panel, (object properties panel of the properties editor), in "Tag:" type in and add `Icon_Hidden`, which will hide the flag mesh from the part tray. The flag mesh's UV map should be square to show the flag correctly, even when the mesh is the right aspect ratio (W = 1.6*H). Set the mu shader of the flag mesh to alpha translucent

For parachutes, the model needs to be made with Y+ being "up", then "adopted" (set child) to an empty object, which is then rotated X+90° so the chute appears correct with Z+up in blender. The semi-deploy and fully deploy animations both need to start at frame 0, with the fully deploy starting position being the same as the end of the semi-deploy anim.

For animation, see this page: https://github.com/taniwha/io_object_mu/wiki/Animating-for-KSP