"""
* pp3.py
* Lu Yu    <<-----  YOU MUST CHANGE the comments and add your name
* luy          <<-----  change to your username
* ECE 2210, Fall 2024
* PP3
*
* NOTE:  You must update all of the following comments!
* 
* Purpose:  A template for PP3 --   YOU MUST CHANGE THIS
*
* Assumptions:
*
* Bugs:  
*
* See the Programming Guide for requirements
"""

# You CANNOT import other modules
import string
from unidecode import unidecode


# Task 1
def words_extraction(filename):
    with open(filename, encoding='utf-8') as file:
        t=file.readlines()
        for x in range(24):
            t.pop(0)
        for x in range(351):
            t.pop(11932)
        t=''.join(t)
        t=t.split()
    for x in range(len(t)):
        y=t[x].strip('“.,”’,?;!_')
        t[x]=y
    for x in range(len(t)):
        for y in range(len(t[x])):
            if t[x].islower()!=True:
                w=[]
                for z in t[x]:
                    w.append(z)
                for l in range(len(w)):
                    if w[l].isupper():
                        k=w[l].lower()
                        w[l]=k
                t[x]=''.join(w)
    return t
            


# Task 2
def histogram_words(lWords):
    d=dict()
    state=0
    for x in lWords:
        state=0
        for y in d:
            if x==y:
                state=1
        if state==1:
            d[x]=d[x]+1
        else:
            d[x]=1
    return d


# Task 3
def sort_histogram(histo):
    d=dict()
    state=0
    for x in lWords:
        state=0
        for y in d:
            if x==y:
                state=1
        if state==1:
            d[x]=d[x]+1
        else:
            d[x]=1
    d=dict(sorted(d.items(), key=lambda item: item[1]))
    d=dict(list(d.items())[-1:-11:-1])
    l=list()
    for key in d:
        l.append(key)
    return l

# Task 4:
def words_in_book_not_list(filename):
    with open('words.txt') as words:
        w=words.read().splitlines()
        s1=set(w)
    d=histogram_words(words_extraction(filename))
    s2=set()
    for key in d.keys():
        s2.add(key)
    s3=s2-s1
    return list(s3)
# The rest of the code is used to test the above functions.
# When you run this script using "$ python3 pp3.py",
# only the code of if-statement below is executed.
# The 'output' file is created by running this script.
if __name__ == '__main__':
    lWords = words_extraction('sherlock.txt')
    histo_words = histogram_words(lWords)
    print('The main text of \"sherlock.txt\" contains %d words.' % len(lWords))
    print('The main text of \"sherlock.txt\" contains %d unique words.' % len(histo_words))
    print('The ten most common words are:')
    print(sort_histogram(histo_words))
    print('There\'re %d unique words in \"sherlock.txt\" but not in \"words.txt\"' % len(words_in_book_not_list('sherlock.txt')))

        



