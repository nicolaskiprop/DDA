import re
import sys


stopwords = [
    "a",
    "an",
    "and",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "was",
    "were",
    "with",
    "I",
    "you",
    "your",
    "we",
    "they",
    "his",
    "her",
    "him",
    "she",
    "me",
    "myself",
    "ourselves",
    "them",
    "themselves",
    "ours",
    "our",
    "who",
    "what",
    "where",
    "when",
    "why",
    "how",
    "which",
    "there",
    "here"
]

for line in sys.stdin:
    line = line.strip()
    line = re.sub(pattern='\W', repl=' ', string=line)
    words = line.split()
    for word in words:
        word = word.lower()
        if word not in stopwords:
            print('%s\t%s' % (word, 1))
 

   