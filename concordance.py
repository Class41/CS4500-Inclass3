# Authors: Daniel Janis, Joel Ascher, Vasyl Onufriyev
#
# Prompt the user for name of external textfile
# --> If the file doesn't exist, prompt descriptive error
#       and reprompt
#
# When textfile is opened, build a list of words that appear
# in the file. (using an unsorted array)
# --> Sort list into alphabetical order
# -->

"""
1. Begin (startApp()) will be main loop
2. Ask for textfile name (readInput()) should handle errors/reprompt
3. Return from readInput() and begin building a list of words (readAndBuild()) using unsorted array
4. Return from readAndBuild(), pass into sorting algorithm
5. Build a list in the following format: Word #oftimesappeared (buildList())
6. Write the output of buildList() to file named: WordCounts.txt, overwrite if exists/create new if not exist
7. Display bargraph of read in data. Resolve ties (displayGraphic())
"""



def startApp():
    print("working")

if __name__ == "__main__":
    startApp()