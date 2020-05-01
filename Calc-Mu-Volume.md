
The “`Calc Mu Volume`” button can be used to calculate the volume of your mesh(es). This can be useful for all sorts of purposes in KSP. It can only be used in Object Mode, and can be used on single or multiple selected mesh objects.

**(NOTE: Currently, it only works on a single parent object, and its immediate children, NOT including any sub-parents. There is an Issue logged on the repo to look into adding multiple object support.)**

It is only used for informational purposes, however, as it does not save the calculation either in the output .mu or .cfg files.

One purpose it can be used for is to determine the volume of fuel and resource tanks, in relation to setting up realistic, or actual, values when setting up your part configs and ModuleManager patches for in-game resource balancing.

To get the most accurate results and proper volume calculation, first make sure that all the object meshes you are performing the calculation on, are closed. This means there should be no open areas in the mesh. Think of it like a real tank: ALL the geometry should be closed up with faces, or it will leak.
Calculating on open meshes is hit or miss, and unreliable, so its best practice to just close everything up.

To get the volume calculation for your object, simply select the object(s) in Object mode, click the “`Apply Scale`” button to make sure all scaling is updated, then click the “`Calc Mu Volume`” button.
The calculated volume for both “Skin Volume” and “External Volume” will be displayed right below the “`Calc Mu Volume`” button, in the status bar.

![](https://i.imgur.com/IkjJgNS.png)

NOTE: On scaling: if at any time before or after calculating the volume of your objects, you make ANY scaling changes to the objects or meshes, you MUST use the “`Apply Scale`” button, to get a correctly refreshed volume calculation.

Taniwha says the “`Apply Scale`” button should ALWAYS be used as a final step, anyway, right before using the “`Export Mu Model`” to export the model, in order to properly calculate and update _**ANY**_ scaling changes made during your model creation.

Taniwha: “The “`Apply Scale`” takes the current local object scale, scales the mesh by it, then sets object scale to 1. Which is why volume updates as expected.
Scale is something you almost never want to leave unapplied, as it messes up all
sorts of things *_especially_* non-uniform scale.”


