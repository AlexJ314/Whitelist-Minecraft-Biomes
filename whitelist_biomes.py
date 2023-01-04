""" Takes a .json object of biome parameters and filters it
  to only desired biomes """

# Get the full biome and parameter list
from file import all_biomes as RAW

# Get the desired biomes list
from file import allow_biomes as ALLOW

def main():
  ''' The main functionality '''

  # Read the full biome list into a Python list
  dirty_biomes = parse(RAW)

  # Filter that list
  clean_biomes = narrow(dirty_biomes, ALLOW)

  # Assemble the filtered biomes back into a .json object
  out = assemble(clean_biomes)

  # Save to a file
  f = open("out.json", "w")
  f.write(out)
  f.close()

  # Done!
  return 0

def parse(string):
  ''' Take a string and break it up into a list of brackets '''

  # Hold each { .... } while we assemble it
  tmp = ""

  # The list to return
  out = []

  # How many brackets deep are we?
  depth = 0

  # Start at ~20 as we assume the all_biomes starts with
  # { "biomes": [
  # and new lines and junk. We just don't want that first bracket

  # For each character in the string...
  for c in string[20:]:

    # Record it
    tmp += c

    # Each element in the list ends with a closing bracket.
    # Is this the closing bracket that matches with the opening bracket?
    if (c == "}"):
      depth -= 1

    # Each element in the list starts with an opening bracket.
    elif (c == "{"):
      depth += 1

    # Have we fully found a { ... } ?
    if (depth == 0):

      # Store it as a list element
      out.append(tmp)

      # Get ready for a new list element
      tmp = ""

  # Return the list!
  return out

def narrow(lst, filt):
  ''' Filter the list by a list of allowed elements '''

  # What to return
  out = []

  # For each element in the list to be filtered...
  for l in lst:

    # Fore each element in the filter...
    for f in filt:

      # If the list element contains an allowed biome...
      if (f in l):

        # Record it!
        out.append(l)

  # Return the filtered list
  return out

def assemble(lst):
  ''' Reassemble the string into something that looks like a .json '''

  # Start the .json off with "biomes": [
  out = "\"biomes\": ["

  # For each { ... } element, except the last one
  for l in lst[:-1]:

    # Record it
    out += l

    # Add a comma
    out += ",\n"

  # Now add the last element, with no comma
  out += lst[-1]

  # Add a newline and close the list
  out += "\n]"

  # Return it!
  return out

if __name__ == "__main__":
  # If this file isn't a sub-module of something, automatically run
  main()
