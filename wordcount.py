#  wordcount.py
#  Jan 2020 (PJW)
#
#  Read a file and count its unique words.
#

import re

infile = 'sample.txt'
outfile = 'counts.txt'

#
#  Set up a regular expression for removing punctuation
#

punct = re.compile(r'\W')

#
#  Open the file and process one line at a time
#

ifh = open(infile,'r')

counts = {}

for line in ifh:

    #  Clean and standardize the line
    
    line  = line.lower()
    line  = punct.sub(' ',line)
    
    #  Split it into words
    
    words = line.split()

    #  Count each use
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

#
#  Print out the results sorted by frequency
#
            
ofh = open(outfile,'w')

for word in sorted(counts,key=counts.get, reverse=True):
    print(word,counts[word],file=ofh)

ofh.close()
