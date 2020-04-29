clearInverse will fix most things being out of place in-game, and apply your scales (crtl A)

create an empty as the 'root' part for your part, and name it the same as your part cfg.in file. child your meshes, colliders, and other transforms(empties) to this (shift drag the objects on top of the root empty). then to export the .mu, select it and press the export mu model button

The exporter will strip all ".xxx" suffixes, so you can have multiple instances of the same name in KSP, even when blender adds the numbered suffix to differentiate different instances with the same name.

Add colliders via 'add mu collider' tab inside the tool menu, or button at top. adjust size on creation, or in Mu Collider panel to adjust colliders size/location, inside the object properties panel of the properties editor, not the blender transform location/rotation/scale
isTrigger for ladders/hatches

use rescaleFactor = 1.0, scale = 1.0,  in your cfg/cfg.in. Otherwise KSP defaults to a 1.25 scale, so a 1m part in blender will come out as a 1.25m part in KSP.

empty objects for nodes (single arrow helps see their rotation, but type doesnt matter). call them node_XXX, or node_attach for srf, outputs in cfg output

Mu Shader panel, textures tab, Name: "_MainTex", under that  change 'grey' to your texture name. same for different maps with entries other than _MainTex

Flag objects, Mu Properties panel, (object properties panel of the properties editor), in "Tag:" add "Icon_Hidden". and mesh's UV map should be square to show the flag correctly, even when the mesh is the right aspect ratio (W = 1.6*H)

for animation with key frames, rotation needs to be in quarternions, not eluer. You can still use eluer to edit, just change to quarternions and blender will convert for you.

once you have your key frames, change the timeline editor to the nonlinear animation editor (or make a new space to have both), and you'll see tracks with the keyframe datd in it. you need to push down the keyframe data into an NLA track, by pressing the button "Push Down Action". You then get a new NlaTrack, and you then double click it's name and rename to what you want the unity animation clip to be called. You can name multiple NlaTracks the same name, and they will all be grouped together and played at once when activated by a KSP module.