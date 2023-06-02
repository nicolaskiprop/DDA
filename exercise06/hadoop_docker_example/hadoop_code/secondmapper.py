import sys

BLUE = '\033[34m'
RESET_COLOR = '\033[0m'

for line in sys.stdin:
    line = line.strip()
    words, numLinks = line.split('\t')
    numLinks = int(numLinks)
    colored_words = f'{BLUE}{words}{RESET_COLOR}'
    print(f'{numLinks}\t{colored_words}')