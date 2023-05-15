import sys

current_node = None
current_count = 0
node_id = None

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from the mapper
    node_id, node, count = line.split()

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Count was not a number, so silently ignore/discard this line
        continue

    # This if-switch only works because the input is sorted by key (here: node_id)
    if current_node == node_id:
        current_count += count
    else:
        if current_node:
            # Write result to STDOUT
            print(f'{current_node} {current_count}')
        current_count = count
        current_node = node_id

print(f'{current_node} {current_count}')
