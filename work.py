import os
from string import punctuation
from collections import Counter
from math import log


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

def main():
    for f in os.listdir('Denison University'):
        file = open('Denison University/'+f,"r", encoding="utf-8")
        x = file.read()
        x = clean_text(x)
        y = counts(x)
        count = 0 
        for i in y:
            count = count + y[i]
        
        z2 = 0
        z = y
        for j in y:
            z[j] = z[j]/count
            if z[j]>z2:
                z2 = z[j]
        print(y['suicide'])
    
##    print(z2)
##    for i4 in y:
##        if y[i4]==z2:
##            print(i4)
##
##
##    file1 = open("b1.txt","r", encoding="utf-8")
##    x1 = file1.read()
##    x1 = clean_text(x1)
##    y1 = counts(x1)
##    count1 = 0 
##    for i1 in y1:
##        count1 = count1 + y1[i1]
##    z1 = y1
##    z21=0
##    for j1 in y1:
##        z1[j1] = z1[j1]/count1
##        if z1[j1]>z21:
##            z21 = z[j1]
##    print(z21)
##    for i5 in y1:
##        if y[i5]==z21:
##            print(i5)
   
    print(count)


main()
