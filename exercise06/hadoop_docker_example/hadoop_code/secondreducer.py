import sys

tuples = []
for line in sys.stdin:
    line = line.strip()
    numLinks, words = line.split('\t')   
    try:
        numLinks = int(numLinks)
        tuples.append((numLinks, words))
    except ValueError:
        continue
#sort tuples by numLinks
sortedTuples = sorted(tuples)
for numLinks, words in sortedTuples:
    print(f'{words}\t{numLinks}')