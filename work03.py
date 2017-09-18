#Work03
#James Smith and Ish Mahdi

import random
global d
d = {}


#CORE FUNCTIONS =============================================================================

#returns a list of the csv file lines.
def open_read(csvFile):
    csv_file = open(csvFile, 'r')
    return csv_file.readlines()[1:len(csv_file.readlines())-1]#exlude the header and footer

def lineToDictEntry(line):
    #This block deals with commas and splicing
    if line.find('''",''') == -1:
        job = line.split(",")[0]
        percentage = line.split(",")[1]

    else:
        job = line.split('''",''')[0][1:]
        percentage = line.split('''",''')[1]
    d[job] = float(percentage)
    return d

#Turns the csv line list into a dictionary with Profession:Percentage
def listToDict(lineList):
    #iterate through the list and fill dictionary
    for line in lineList:
        lineToDictEntry(line)

#Picks weighted random key value from dictionary
def getRandom():
    threshold = random.random() * 99.8#total percentage
    counter = 0
    for entry in d:
        counter += d[entry]
        if(counter > threshold):
            return entry
#CORE FUNCTIONS ===========================================================================

#TESTING FUNCTIONS ========================================================================
def printAll(dic):
    for entry in dic:
        print entry, dic[entry]

#prints a dictionary with the difference between the percentage frequency(in whole numbers) of the random algo and the given weights. Slightly off because the total of the given is out of 99.8 while the algo calculation is out of 100
def testRandom(numSamples):
    c = {}
    counter = 0
    for entry in d:
        c[entry] = float(0)
    while(counter < numSamples):
        rand = getRandom()
        c[rand] += 1
        counter += 1
    for entry in c:
        c[entry] = (c[entry] /float(numSamples)) * 100
    difDict = {}
    for entry in d:
        difDict[entry] = c[entry] - d[entry]
    printAll(difDict)

#TESTING FUNCTIONS ========================================================================

#testing program
def run(csvFile):
    lineList = open_read(csvFile)
    listToDict(lineList)
    #testRandom(100000) #use to see the randomness of the algorithm
    print(getRandom())

run("occupations.csv")        
