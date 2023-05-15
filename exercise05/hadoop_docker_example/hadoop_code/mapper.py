import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into node ID and neighbors
    node, n = line.split(':')
    neighbors = n.split(',')

    # Count the neighbors of the node
    neighbor_count = sum([int(neighbor) for neighbor in neighbors])

    # Write the results to STDOUT (standard output)
    # Each line will contain node ID, node ID, and neighbor count
    print(f'{node} {node} {neighbor_count}')
