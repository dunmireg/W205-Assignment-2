

wordsDict = {}
numFiles = 47
hashtag = "#NBAFinals2015 #Warriors"

for i in range(0, numFiles):
    fname = hashtag+"-tweetsText-"+str(i+1) +".txt"
    curr = open(fname, 'r')
    text = curr.read()
    curr.close()
    words = list(text.split())

    for w in words:
        if w not in wordsDict:
            wordsDict[w] = 1
        else:
            wordsDict[w] += 1

curr = open("wordCounts.csv", "w")
for word, count in wordsDict.iteritems():
    curr.write('"' + word + '", ' + str(count) +'\n')
curr.close()
