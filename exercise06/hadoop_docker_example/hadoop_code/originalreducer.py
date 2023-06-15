import sys
treshold = 100
linkCounter = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    if count > treshold:
        print(f'{word}\t{count}')


#     linkCounter += 1
# print(f'Number of links: {linkCounter}')

# import sys
# for line in sys.stdin:
#     line = line.strip()
#     print(line)