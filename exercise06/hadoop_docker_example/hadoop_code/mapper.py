import re
import sys
from collections import defaultdict

stopwords = [
    "a", "an", "and", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is",
    "it", "its", "of", "on", "that", "the", "to", "was", "were", "with", "I", "you",
    "your", "we", "they", "his", "her", "him", "she", "me", "myself", "ourselves",
    "them", "themselves", "ours", "our", "who", "what", "where", "when", "why", "how",
    "which", "there", "here"
]

linksCount = defaultdict(set)
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = re.sub(pattern='\W', repl=' ', string=line)
    line = re.sub(pattern='\s+', repl=' ', string=line)
    words = line.split()
    filteredWords = [word for word in words if word not in stopwords]
    line= ' '.join(filteredWords)

    if not line:
        continue

    tokens = line.split()
    for n in range(1, len(tokens) + 1):
        numTokens = len(tokens)
        for i in range(numTokens - n + 1):
            wordTuple = tuple(tokens[i:i+n])
            Word = wordTuple[0]
            linksCount[Word].update(wordTuple[1:])

for Word in linksCount:
    numLinks = len(linksCount[Word])
    print(f'{Word}\t{numLinks}')


#part 1
# import re
# import sys

# stopwords = [
#     "a", "an", "and", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is",
#     "it", "its", "of", "on", "that", "the", "to", "was", "were", "with", "I", "you",
#     "your", "we", "they", "his", "her", "him", "she", "me", "myself", "ourselves",
#     "them", "themselves", "ours", "our", "who", "what", "where", "when", "why", "how",
#     "which", "there", "here"
# ]

# for line in sys.stdin:
#     line = line.strip()
#     line = line.lower()
#     line = re.sub(pattern='\W', repl=' ', string=line)
#     line = re.sub(pattern='\s+', repl=' ', string=line)
#     words = line.split()
#     filteredWords = [word for word in words if word not in stopwords]
#     line = ' '.join(filteredWords)
#     print(line)