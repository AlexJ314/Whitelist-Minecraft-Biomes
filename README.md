
# Welcome to a biome black/whitelister for Minecraft 1.19!
# *TL;DR: How to generate a Minecraft world of only certain biomes.*

Used to generate a list of biomes and their parameters from a specific set of selected biomes. This can then be pasted into a .json and used in a datapack for Minecraft. It should work for versions 1.16 and up.

**Of note: Terrain generation appears to be unaffected as Minecraft first generates terrain and then assigns it a biome. This biome then impacts structure generation, mob spawning, biome color, and other such features.**
      
To change terrain generation, edit the .json files within the `noise_settings` folder of the datapack later during creation.
    
## How to use:

### Generate your biome list

Edit `config.py` so `biomelist` contains the name of every biome you want to either include or exclude, including the vanilla/mod namespace, e.g. `minecraft:frozen_river`, or `byg:autumn_forest`, or any other `mod_name:biome_name`.

To work with modded biomes, add them to `biomelist.json` alongside vanilla biomes.

Run `main.py`, specifying -m for --mode - "include" to whitelist your biomes, or "exclude" to blacklist them. The resulting biome JSON will appear at `out.json`

### Prepare your datapack

Find datapack examples [here](https://github.com/slicedlime/examples) and [here](https://drive.google.com/drive/folders/1F8F8gFyy6oy4WVcMiDNd_8cFTnNjromP).

Get a datapack there or start your own, find `normal.json` or your desired worldgen option under `worldgen/world_preset` and replace the `"preset": "minecraft:overworld"` field with `"biomes": ` followed by the contents of `out.json`.

Example:
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

To complete your pack, refer to [the wiki page](https://minecraft.fandom.com/wiki/Data_pack) and [tutorial](https://minecraft.fandom.com/wiki/Tutorials/Creating_a_data_pack)

*This is not in any way endorsed by Mojang or any of their affiliates*