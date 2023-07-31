import argparse
import importlib
import json

ap = argparse.ArgumentParser(
    prog="biome_JSON_generator",
    description="This program generates a list of biomes with vanilla-like generation either excluding your list or ONLY including from your list.")

ap.add_argument('-m', "--mode", help='whether to "include" or "exclude"; default "exclude', type=str, default="exclude")
ap.add_argument('-f', '--from', help='where to get the biome list to include or exclude; default "config" NB! do not use an extension', type=str, default='config')

args = vars(ap.parse_args())

try:
    source_name = args['from']
    source = importlib.import_module(source_name)
    userbiomes = set(source.biomelist)
except:
    raise Exception(f'No file at {args["from"]}, or no "biomelist" in the file specified')

if args['mode'] not in ['include', 'exclude']: raise Exception("Invalid mode selected")
KEEP_LIST = False if args['mode'] == "exclude" else True

with open('biomelist.json', 'r') as biomesrc:
    all_biomes = json.load(biomesrc)

out = []
for biomedef in all_biomes:
    current_name = biomedef['biome']
    is_present = True if current_name in userbiomes else False
    if is_present and KEEP_LIST:
        out.append(biomedef)
    elif not is_present and not KEEP_LIST:
        out.append(biomedef)

with open("out.json", 'w') as trg:
    json.dump(out, trg, indent=4, sort_keys=True)