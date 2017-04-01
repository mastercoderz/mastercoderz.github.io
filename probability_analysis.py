import os
from string import punctuation
from collections import Counter
from string import punctuation
from stop_words import get_stop_words
from heapq import heappush, heappop  #import heapq library
from math import log
from bs4 import BeautifulSoup
import matplotlib.pyplot as pyplot

#==================================
# Takes a text file and strips it of punctuation
#   , uppercase, and "stop" words
def clean_text(file):
    fileText = file.split()
    stop_words = get_stop_words('english')
    allWords = []
    for word in fileText:
        if word not in stop_words:
            word = word.strip().strip(punctuation).strip().lower()
            allWords.append(word)   
    return allWords

#==================================
# Takes a text file and strips it of punctuation
#   , uppercase, and "stop" words
def counts(l):
    doc_count = Counter()
    tree_count = Counter()
    tree_count.update(l)      
    doc_count.update(set(l))  
    return tree_count

#==================================
# Find the intersection between
# groupwords and baseword lists
# return it
def intersect(groupWords, baseWords):
    intersection = []
    for word in groupWords:
        if word in baseWords:
            intersection.append(word)
    
    return intersection

#==================================
# return base library
def buildLibrary(countsDict, libSize):        # input parameter is dict
    heap = []           # initialize our heap
    list = []
    for key in countsDict:       
        heappush(heap, (-countsDict[key], key))
        
    if len(heap) < libSize:
        heaplength = len(heap)
    else:
        heaplength = libSize
        
    for i in range (0,heaplength):
        if len(heap) > 0:
            tup = heappop(heap)
            list.append(tup[1]) #pop 10,000 most used words in the file
            #print(-tup[0], ":", tup[1]) # heappop(heap)[1])
    return list

#==================================
# given a file list, build the base library
# after making the dictionary of counts
def getBaseLibrary(fileList):
    allWords = buildWordList(fileList)
    countsDict = counts(allWords)
    return buildLibrary(countsDict, 5000)

#==================================
# Take a list of files, return word list
# for all files combined
def buildWordList(fileList):
    allWords = []
    for f in fileList:
        file = open(f, "r")
        fileString = file.read()
        cleanedList = clean_text(fileString)
        allWords += cleanedList
    return allWords

#==================================
# Take a dictionary of probabilities
# return a list with 20 words whose
# probability of use changed the most
def top20(dict):    # takes as input a dictionary storing each word and its change in delta
    heap = []
    list = []       # initiate our output list
    for key in dict:
        heappush(heap, (-dict[key], key))    # (change in delta, word)

    for i in range (0,20):
        if len(heap) > 0:
            tup = heappop(heap)
            print(-tup[0], ":", tup[1]) # heappop(heap)[1])
    return list

def getFileList(year1, year2):
    nameList1 = []
    nameList2 = []
    for f in os.listdir('Denison University'):
        file = open('Denison University/'+f,"r", encoding="utf-8")
        x = file.read()
        soup = BeautifulSoup( x, 'html.parser' )
        dataTag = soup.find('date')
        if dataTag.text[0:4] == year1:
            print("file for",year1,"=", f)
            nameList1.append(f)
        elif dataTag.text[0:4] == year2:
            print("file for", year2, "=", f)
            nameList2.append(f)
        file.close()

    return nameList1, nameList2

def main():
    
    fileList = ["pride.txt"] #put our primary corpus files in here
    baseLib = getBaseLibrary(fileList)
    #we have base library now

    #to modify/expand this, write a program that'd be called in here
    #to grab names of newspaper files for given time periods 

    #put file strings in these lists:
    group1, group2 = getFileList("1950", "2000")
    

    #grab word lists for each group of files
    wordList1 = buildWordList(group1)
    wordList2 = buildWordList(group2)

    #filter lists so they only include words from the base library
    wordList1 = intersect(wordList1, baseLib)
    wordList2 = intersect(wordList2, baseLib)

    CountsDict1 = counts(wordList1)
    CountsDict2 = counts(wordList2)

    #=====================================================================
    #  1. Get data pools (group1, group2)
    #  2. Modify data pools using intersectSets with base lib
    #  3. Establish word counts for each respective group
    #  4. Loop through each group and calculate prob. of word occurring
    #       in that group (do this for every word)
    #  5. Store dict = {word : (prob group, prob overall)}, for each group
    #  6. determine change in probabilities between groups for every word
    #       compare this change 
    #  7. Pick the top 20 words whose delta probability is highest (use pq
    #       again)
    #  8. Use log likelihood calculations to determine a better measure of
    #       the probaiblity of the words appearing
    #  9. Infer cool things about what caused changes in word appearance
    #       over time
    #======================================================================

main()
