
# Welcome to a biome whitelister for Minecraft 1.19!


# TL;DR: How to generate a Minecraft world of only certain biomes.

*Or, How to make a Minecraft world of only biomes I want*


## What this is:

  
  Used to generate a list of biomes and their parameters from a specific set of
    selected biomes. This can then be pasted into a .json and used in a
    datapack for Minecraft. It should work for versions 1.16 and up.

  **Of note: Terrain generation appears to be unaffected as Minecraft first
    generates terrain and then assigns it a biome. This biome then impacts
    structure generation, mob spawning, biome color, and other such features.**
  
    
    
  To change terrain generation, edit the .json files within the
    `noise_settings` folder. (see below)
    


## How to use:

  
  Edit `file.py` such that `allow_biomes = ["your biome", "other biome"]`
    contains all the biomes you want allowed. Of note, `minecraft:ocean` will
    only allow the ocean biome, while `ocean` will allow the ocean biome and
    its variants, such as `frozen_ocean`, or `deep_lukewarm_ocean`.  
    The default file whitelists ocean-like biomes.
  

  
  Edit `file.py` such that `all_biomes` is a multiline string of all the of the
    default biomes and their parameters. This code works under the assumption
    that you have a list of all vanilla generation biomes. This list can be 
    found at
    https://github.com/Arcensoth/mcdata/tree/master/generated/reports/biome_parameters/minecraft
  
    
    
  More vanilla world generation can be found at
    https://github.com/slicedlime/examples
    

    
  The default file includes the 1.19 biome generation parameters
    

  
  Once set, simply run whitelist_biomes.py.
    This will generate the `out.json` file.
  

  
  From here, find `normal.json` within the `world_preset` folder and edit it
    such that `"preset": "minecraft:overworld"` is replaced by the entire
    contents of `out.json`.
  

  
  Save `normal.json` and launch Minecraft. When creating a new world, add
    your datapack with these changes to the world. Cycle through the world
    presets until you come back to `Default`. Now you can generate the world
    with your custom biomes as a preset.
  


## Using this as a datapack:

  
  The above assumes you already have a solid grasp of datapacks.

  Here we'll go into more detail. A more general tutorial can be found at
    https://minecraft.fandom.com/wiki/Tutorials/Creating_a_data_pack
  

  
  Download https://github.com/slicedlime/examples/raw/master/vanilla_worldgen.zip
    to obtain the default world generation settings. Previous Minecraft
    versions are available under `commits`.
  

  
  Extract this zip to `vanilla_worldgen`
  

  
  Create a new folder where you like named `mydatapack`
  

  
  Create a new folder within `mydatapack` named `data`
  

  
  Create a new folder within `data` named `minecraft`  
    This will overwrite Minecraft defaults with any edits you make.
    Because of this, it is recommended that you delete any files you haven't
    edited.
  

  
  Copy the `worldgen` folder from `vanilla_worldgen` into `minecraft`
  

  
  Delete all folders within `worldgen` except for `world_preset`
  

  
  Delete all files within `world_preset` except for `normal.json`
  

  
  Other files and folders can be kept if you wish to edit them instead.  
    For example, to change the sea level in a world, keep the `noise_settings`
    folder and `overworld.json`. Then find `sea_level: 63` and change it to
    `sea_level: 100` to change the default sea level to 100.
  

    
  **Note: sea mob generation is still capped at y 63.**
    

    
  These .json files control the noise settings used under the `settings: `
    tag found in the `world_preset` files. Changes here will impact terrain
    generation.
    

  
  Within the `normal.json` file, after running `whitelist_biomes.py`,
    paste the entire contents of `out.json` over
    `"preset": "minecraft:overworld"`
  

  
  Your `normal.json` should now look something like below.  
    Biomes may be repeated several times as they can have different parameters.  
    The spacing / formatting will look atrocious, but you can auto-style it
    or leave it as is.
  
  ```
{
  "dimensions": {
    "minecraft:overworld": {
      "type": "minecraft:overworld",
      "generator": {
        "type": "minecraft:noise",
        "settings": "minecraft:sealevel_overworld",
        "biome_source": {
          "type": "minecraft:multi_noise",
          "biomes": [
            {
              "biome": "minecraft:lush_caves",
              "parameters": {
                "temperature": [
                  -1,
                  1
                ],
                "humidity": [
                  0.7,
                  1
                ],
                "continentalness": [
                  -1,
                  1
                ],
                "erosion": [
                  -1,
                  1
                ],
                "weirdness": [
                  -1,
                  1
                ],
                "depth": [
                  0.2,
                  0.9
                ],
                "offset": 0
              }
            },
            {
              "biome": "minecraft:deep_dark",
              "parameters": {
                "temperature": [
                  -1,
                  1
                ],
                "humidity": [
                  -1,
                  1
                ],
                "continentalness": [
                  -1,
                  1
                ],
                "erosion": [
                  -1,
                  -0.375
                ],
                "weirdness": [
                  -1,
                  1
                ],
                "depth": 1.1,
                "offset": 0
              }
            }
          ]
        }
      }
    },
    "minecraft:the_end": {
      "type": "minecraft:the_end",
      "generator": {
        "type": "minecraft:noise",
        "settings": "minecraft:end",
        "biome_source": {
          "type": "minecraft:the_end"
        }
      }
    },
    "minecraft:the_nether": {
      "type": "minecraft:the_nether",
      "generator": {
        "type": "minecraft:noise",
        "settings": "minecraft:nether",
        "biome_source": {
          "type": "minecraft:multi_noise",
          "preset": "minecraft:nether"
        }
      }
    }
  }
}
  ```

  
  **Of note: If you wish to create multiple dimensions, that can be done here, too.  
    Simply copy / paste new dimensions or write your own, making sure
    their names are unique. The `settings` tag references a .json file within
    `noise_settings`. You may modify, rewrite, or create your own settings file.**
  

  
  Return to the `mydatapack` folder
  

  
  Here, next to the `data` folder, create a file named `pack.mcmeta`
  
  
  
  Open `pack.mcmeta` and paste the following:
  

  ```
{
  "pack": {
    "pack_format": 10,
    "description": "I made a datapack!!!"
  }
}
  ```

  
  You may also create an icon for the pack here in the form of a
    128 x 128 pixel image. Save it as `pack.png`.
  
  
  I've also included a demo datapack of only ocean-y biomes with an
    increased sea level, along with some extra dimensions. As per 
    https://minecraft.fandom.com/wiki/Custom_dimension,  
    "New dimensions added can be accessed currently only by using commands,
    like `/execute in <dimension> run teleport <coordinates>`."

  
  After launching Minecraft and preparing to create a world,
    paste the `mydatapack` folder into the `datapacks` subfolder of the
    world being created. This must be done prior to world generation.
  

  
  As described before, cycle through the world presets and select `Default`.  
    A full cycle must occur, otherwise the true default world generation will
    be used instead of our modified default.
  

## Final thoughts:

  I've also included `blacklist_biomes.py` to instead exclude listed biomes.
    The use is still the same as `whitelist_biomes.py`.
  
  Be sure to check out https://minecraft.fandom.com/wiki/Minecraft_Wiki
    if you have additional questions. Happy modding!
  

  
  *This tutorial is in no way affiliated with anything*
  
