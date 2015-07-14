import sys
from collections import Counter
if len(sys.argv) < 3:
	print("Invalid arguments")
	sys.exit()

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

count = Counter()  #Counter object implements an efficient hash based counting
for tweet in fin:
	count += Counter(tweet.split())

for tuple in sorted(count.items()):
	fout.write(str(tuple[0]) + "\t" + str(tuple[1]) + "\n")