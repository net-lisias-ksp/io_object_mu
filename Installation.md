# Installation Instructions

If you don't have Git already, [you can download it from here.](https://git-scm.com/downloads)

1. Clone this repository into your preferred location. ([To clone a repository, you can follow these steps](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Copy the entire `io_object_mu` folder into Blender's `scripts/addons` folder.
    1. For Windows users, this is `C:\Program Files\Blender Foundation\Blender <version>\<version>\scripts\addons`
    2. For Linux users, this is `~/.config/blender/<version>/scripts/addons`.
3. Start Blender.
4. Go to Edit -> Preferences... -> Add-ons tab.
5. Type `ksp` into the search box and find `Import-Export: Mu model format (KSP)` in the list.
6. Check the checkbox on the left of the list item.
7. Optionally, click on the little triangle on the left of the list item: it will open additional settings. Here you can set the KSP `GameData` directory (required for craft import), install shader presets (recommended), configuration template files, and some color palettes.
8. Optionally click "Save Preferences" hidden in the hamburger menu button in the lower left of the preferences window.

If you now go to the File -> Import menu, it should have `KSP Craft (.craft)` and `KSP Mu (.mu)` at the bottom of the list, and in the File -> Export menu, `KSP Mu (.mu)`.

## Symbolic links

If you don't want to copy the `io_object_mu` folder every time it has new changes, then you can create a symbolic link.

### Windows
1. Open the command prompt as administrator, otherwise it won't work.
2. Type the following command: **Change the paths according to your paths.**
```
mklink /D "C:\Program Files\Blender Foundation\Blender 2.92\2.92\scripts\addons\io_object_mu" D:\GitHub\io_object_mu
```

### Linux
1. Open your terminal.
2. Type the following command: **Change the paths according to your paths.**
```
$ ln -s /home/github/io_object_mu ~/.config/blender/2.83/scripts/addons/io_object_mu
```

# Updating the files

To keep you files updated you can use the fetch / pull commands.

1. Open your terminal.
2. Change the current working directory to the location where you have the cloned directory.
3. Type the following command:
```
$ git fetch origin
```

4. Press **Enter** to fetch the lastest changes in the repository.
```
$ git fetch origin
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (3/3), 8.94 KiB | 84.00 KiB/s, done.
From https://github.com/taniwha/io_object_mu
   baa00d961..db1d88ca4  master     -> origin/master
```

5. If it's done fetching the changes, type the following command:
```
$ git pull origin master
```

6. Press **Enter** to apply the changes into your directory.
```
$ git pull origin master
From https://github.com/taniwha/io_object_mu
 * branch                master     -> FETCH_HEAD
Updating baa00d961..db1d88ca4
Fast-forward
 export_mu/light.py | 3 ++-
 import_mu/light.py | 3 ++-
 2 files changed, 4 insertions(+), 2 deletions(-)
```