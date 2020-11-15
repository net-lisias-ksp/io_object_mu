Firstly for animation with key frames, rotation needs to be in quarternions, not eluer. You can still use eluer to edit, just change to quarternions **before applying keyframes** and blender will convert for you:

![](https://i.imgur.com/Pa0EcuJ.png)

"taniwha: if doing continuous rotations, because unity's curves are quaternion-only, you need to animate two full revolutions (in steps < 1 revolution) to avoid weird things happening at each revolution"

Next ether change the timeline editor to the nonlinear animation editor, or make a new space to have both:

![](https://i.imgur.com/nVvOStZ.png)

Then you'll see "actions" with the keyframe data in them:
 
![](https://i.imgur.com/R1C7hTo.png)

Then you need to push down the keyframe data into an NLA track, by pressing the button `Push Down Action`:

![](https://i.imgur.com/OTEuL2a.png)

All tracks need to start at frame 0, for example semi and fully deploy parachute animations, both need to start at 0 even if you make them one after another.

Then double click the NLA track's name and rename to what you want the unity animation clip to be called:

![](https://i.imgur.com/4aqdrBg.png)

You can name multiple NlaTracks the same name, and they will all be grouped together by the exporter, and played as one animation when activated by a KSP module. You don't need to merge them in blender (you can't anyway)

You can still edit the keyframes of an NLA track by selecting the track so it's yellow, and pressing tab or right click it - `start tweaking strip actions` (it should turn green). Then you can just edit or add keyframes as normal:

![](https://i.imgur.com/7CCzEVA.png)

You can convert an animation to quarts by using a dummy object with constraints and animation baking:

0) animate the thing you want
1) make a new object/mesh/whatever
2) add a constraint to the new object, copy rotation, and set the animated object as the source
3) bake that constraint animation, so it doesn't have a constraint anymore, just its own keyframes (keys every frame)
4) then, set the original thing to use quart rotations in the transform panel, and then repeat the last 2 steps, this time constraining the original object's rotation to the dummy objects. then bake the animation again, but this time since it's set to quarts, it'll key in quarts!