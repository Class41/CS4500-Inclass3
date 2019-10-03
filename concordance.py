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
3. Return from readInput() and begin building a list of words (buildList()) using unsorted array
4. Return from buildList(), pass into sorting algorithm
5. Build a list in the following format: Word #oftimesappeared (buildList())
6. Write the output of buildList() to file named: WordCounts.txt, overwrite if exists/create new if not exist (writeListToFile())
7. Display bargraph of read in data. Resolve ties (displayGraphic())
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#def readInput():















# BuildList() will takes in a list as a parameter and should count word occurrences 

#def buildList():











#def writeListToFile():


















def displayGraphic():
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()
















#Main function (python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose)
def startApp():
    #wordList = readInput() #returns an unsorted wordlist ["word1", "word2", "word3"]
    #sortedCountedList = buildList(wordList) #returns a sorted array with counts [["word1", 10], ["word2", 5], ["word3", 2]]
    #writeListToFile(sortedCountedList) #writes file to list

    displayGraphic("""sortedCountedList""") #displays graphic

if __name__ == "__main__":
    startApp()