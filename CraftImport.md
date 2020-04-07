Importing Craft Files
=========

In order to import craft files, `io_object_mu` first needs to know where to look for KSP's data files. This is achieved by configuring the KSP `GameData` directory in the addon's settings panel (see [Installation](https://github.com/taniwha/io_object_mu/wiki/Installation)).

The craft importer understands KSP's part config files, including MODEL nodes, and because it uses the actual `.mu` import code to load the models, any part for which the component models can be successfully imported manual can be imported.

Also, Module Manager is supported: when reading KSP part config files, the craft importer first checks for Module Manager's `ModuleManager.ConfigCache` and if found, parses that instead of the `.cfg` files scattered throughout `GameData`. This does indeed mean that modded are supported.

However, KSP's variants and other part-switching mods are not yet supported.

# The imported craft
Once imported, the craft is presented as a single monolithic object: the individual parts, submodels, etc cannot be selected. This is for ease of manipulation of the entire craft. However, it is possible to access everything down to the individual meshes:
* In blender's outliner (upper right corner panel in the default layout), select "Scenes" in the second dropdown (defaults to View Layers, looks a little like a pile of photos), just to the left of the search box.
* Click on the mu_utils scene to switch to it, and also open it by clicking its triangle.
* In there, you will find Scene Collection: open it.
* Under that, there is craft_collection, which is where the assembled craft is stored (in its own collection under craft_collection).  You will have to enable display and selection for the collection (this may require adjusting the collection filter settings via the funnel icon).
* You will also find loaded_parts which stores assembled parts (some parts are built from multiple models) and loaded_models (the actual models as loaded from .mu files).
