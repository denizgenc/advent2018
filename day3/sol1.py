import re
from itertools import chain
fabric = [[0 for i in range(1000)] for j in range(1000)]
claim_re = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open("input.txt") as f:
    for claim in f:
        matches = claim_re.search(claim)
        begin_row = int(matches.group(2))
        begin_col = int(matches.group(3))
        width = int(matches.group(4))
        height = int(matches.group(5))
        for row in range(begin_row, begin_row + width):
            for column in range(begin_col, begin_col + height):
                cell = fabric[row][column]
                if cell == 0 or cell == 1:   # If fabric not used yet: 0 -> 1
                    fabric[row][column] += 1 # if already used: 1 -> 2
print([i for i in chain.from_iterable(fabric)].count(2))
    # chain.from_iterable basically flattens the array of arrays and turns it into a long line
