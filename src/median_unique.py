import sys
from collections import Counter
if len(sys.argv) < 3:
    print("Invalid arguments")
    sys.exit()

def getMedian(inlist):
    inlist.sort()
    length = len(inlist)
    if length % 2 != 0: 
        midl = (length / 2)
        res = inlist[midl]
    else:
        odd = (length / 2) -1
        ev = (length / 2) 
        res = float(inlist[odd] + inlist[ev]) / float(2)
    return res


fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

count = []
for tweet in fin:
    count.append(len(Counter(tweet.split()).keys()))
    fout.write(str(getMedian(count)) + "\n")