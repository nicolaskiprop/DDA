import sys
import re

current_target = None
current_sources = []
target = None
sources = []

#input comes from STDIN
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    #parse the input we got from mapper.py
    target, source = line.split('[')
    sources = source.split('')
    sources = re.sub(pattern='\W', repl=' ', string=sources)


    if current_target == target:
        for s in sources:
            if s not in current_sources:
                current_sources.append(s)
            else:
                if current_target:
                    if len(current_target) > 100:
                        print(f'{current_target} {len(current_sources)}')
                        current_target = target
                        current_sources = sources

            if len(current_sources) > 100:
                print(f'{current_target} {len(current_sources)}')
                current_target = target
                current_sources = sources