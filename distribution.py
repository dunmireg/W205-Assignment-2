import os.path
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
import codecs
import pylab as pl
import numpy as np

if not os.path.exists("result.txt"):
    hashtag = "#NBAFinals2015"
    num_files = 108
    list_of_files = []

    for i in range(0, num_files):
        fname = fname = hashtag+"-tweetsText-"+str(i+1) +".txt"
        list_of_files.append(fname)

    with open("result.txt", "wb") as outfile:
        for f in list_of_files:
            with open(f, "rb") as infile:
                for line in infile:
                    line = line.lower()
                    outfile.write(line)

file = codecs.open("result.txt", "r", "utf-8")
text = file.read()
tokens = nltk.word_tokenize(text)
fdist = FreqDist(tokens)
common = fdist.most_common(1000)
stopwords = nltk.corpus.stopwords.words('english')
fdist2 = {}
i = 0

while len(fdist2) <= 30:
    curr = common[i]
    if curr[0] not in stopwords:
        fdist2[curr[0].encode('ascii')] = curr[1]
    i += 1

X = np.arange(len(fdist2))
pl.bar(X, fdist2.values(), align = 'center', width = 0.5)
pl.xticks(X, fdist2.keys())
ymax = max(fdist2.values()) + 1
pl.ylim(0, ymax)
pl.show()

#d = {'CLOVER':4,'SPADE':6,'DIAMOND':7,'HEART':2}
#X = np.arange(len(d))
#pl.bar(X, d.values(), align='center', width=0.5)
#pl.xticks(X, d.keys())
#ymax = max(d.values()) + 1
#pl.ylim(0, ymax)
#pl.show()
