import os
from string import punctuation
from collections import Counter
from math import log
import matplotlib.pyplot as pyplot
from bs4 import BeautifulSoup




def clean_text(text):
    words = text.split()
    words = [w.strip().strip(punctuation).strip().lower()
             for w in words]
    words = [w for w in words 
             if w                  # remove empty strings
             and w != 'p'          # remove stray HTML <p> tags
             and w != 'gt'         # remove stray HTML entities
             and w != 'lt'
             and w != 't'          # remove stray contraction tails
             and w != 's'          # remove stray possesives...
             and not any(c.isdigit() for c in w)]  # ...and numbers.
    return words

def counts(l):
    doc_count = Counter()
    tree_count = Counter()
    tree_count.update(l)      # Add these words to the existing totals
    doc_count.update(set(l))  # `set` eliminates duplicates. That way, 
                                          # each document only counts once at most.
    # We also want to know the total number of documents and a list 
    # of all the words in all the documents:
#    n_docs = len(l) + len(notreetext)
#    all_words = set(tree_count) | set(notree_count)
    return tree_count
def graphForDenison():
    xvaluesDU = []
    yvaluesDU = []
    for f in os.listdir('Denison University'):
        file = open('Denison University/'+f,"r", encoding="utf-8")
        x = file.read()
        x1 = clean_text(x)
        y = counts(x1)
        soup = BeautifulSoup( x, 'html.parser' )
        dataTag = soup.find('date')
        xvaluesDU.append(dataTag.text[0:4])
        yvaluesDU.append(y['suicide'])
        pyplot.plot(xvaluesDU, yvaluesDU)
        pyplot.show()

def graphForKenyon():

    xvaluesKC = []
    yvaluesKC = []
    for f1 in os.listdir('Kenyon College'):
        file = open('Denison University/'+f1,"r", encoding="utf-8")
        x = file.read()
        x1 = clean_text(x)
        y = counts(x1)
        soup = BeautifulSoup( x, 'html.parser' )
        dataTag = soup.find('date')
        xvaluesKC.append(dataTag.text[0:4])
        yvaluesKC.append(y['suicide'])
    pyplot.plot(xvaluesKC, yvaluesKC)
    pyplot.show()

def graphForOberlinCollege():
    
    xvaluesOWU = []
    yvaluesOWU = []
    for f3 in os.listdir('Ohio Wesleyan University'):
        file = open('Ohio Wesleyan University/'+f3,"r", encoding="utf-8")
        x = file.read()
        x1 = clean_text(x)
        y = counts(x1)
        soup = BeautifulSoup( x, 'html.parser' )
        dataTag = soup.find('date')
        xvaluesOWU.append(dataTag.text[0:4])
        yvaluesOWU.append(y['suicide'])
    pyplot.plot(xvaluesOWU, yvaluesOWU)
    pyplot.show()

def Ohio Wesleyan University():
    xvaluesOC = []
    yvaluesOC = []
    for f2 in os.listdir('Oberlin College'):
        file = open('Oberlin College/'+f2,"r", encoding="utf-8")
        x = file.read()
        x1 = clean_text(x)
        y = counts(x1)
        soup = BeautifulSoup( x, 'html.parser' )
        dataTag = soup.find('date')
        xvaluesOC.append(dataTag.text[0:4])
        yvaluesOC.append(y['suicide'])
    pyplot.scatter(xvaluesOC, yvaluesOC)
    pyplot.show()    
    
def main():
    
    graphForDenison()
    graphForKenyon()
    graphForOberlinCollege()
    Ohio Wesleyan University()

       
 

main()
