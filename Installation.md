Installation Instructions
=========================

1. Clone the github repository. It is best to clone the repository rather than downloading the zip file provided by github because the zip file can have a `.` in the directory name (particularly if the blender2.79 branch is downloaded) and due to limitations in the Python language, Blender is unable to import addons that have `.` in the directory name. Also, cloning the repository makes updating trivial: just a `git pull` in the `io_object_mu` directory.
1. Copy the entire folder (`io_object_mu`) into Blender's `scripts/addons` folder. For Linux users, this is `~/.config/blender/<blender-version>/scripts/addons`.
1. Start Blender
1. Go to Edit ->  Preferences... -> Add-ons tab
1. Type `ksp` into the search box and find "Import-Export: Mu model format (KSP)" in the list
1. Check the checkbox on the left of the list item.
1. Optionally, click on the little triangle on the left of the list item: it will open additional settings. Here you can set the KSP `GameData` directory (required for craft import), install shader presets (recommended), configuration template files, and some color palettes.
1. Optionally click "Save Preferences" hidden in the menu button in the lower left of the preferences window.

If you go to the File -> Import menu, it now has "KSP Mu" and "KSP Craft" in the list, and File -> Export menu now has "KSP Mu".