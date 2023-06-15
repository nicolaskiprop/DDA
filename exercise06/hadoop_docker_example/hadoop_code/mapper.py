import re
import sys

stopwords = ["a", "an", "and", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is",
    "it", "its", "of", "on", "that", "the", "to", "was", "were", "with", "I", "you",
    "your", "we", "they", "his", "her", "him", "she", "me", "myself", "ourselves",
    "them", "themselves", "ours", "our", "who", "what", "where", "when", "why", "how",
    "which", "there", "here"]

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = re.sub(pattern='\W', repl=' ', string=line)
    line = re.sub(pattern='\s+', repl=' ', string=line)
    words = line.split()
    filteredWords = [word for word in words if word not in stopwords]
    line = ' '.join(filteredWords)
    print(line)
    
    for i, word in enumerate(words):
        #write the results to STDOUT (standard output);
        #what we output here will be the input for the reducer
        #if te word is not the first word in the line, output the word as target
        if i > 0:
            value = [word[i-1]]
            print('%s\t%s' % (word, value))

        #extend te word tuple to include the word before te previous word
        if i > 1:
            value = [word[i-2]]
            print('%s\t%s' % (word, value))
        
        #extend te word tuple to include the word before te previous word
        if i > 2:
            value = [word[i-3]]
            print('%s\t%s' % (word, value))
        #extend te word tuple to include the word before te previous word  
        if i > 3:
            value = [word[i-4]]
            print('%s\t%s' % (word, value))
        #extend te word tuple to include the word before te previous word
        if i > 4:
            value = [word[i-5]]
            print('%s\t%s' % (word, value))