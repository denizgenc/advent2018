import re
from itertools import chain
fabric = [[0 for i in range(1000)] for j in range(1000)]
claim_re = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

non_overlapping = []

with open("input.txt") as f:
    for claim in f:
        matches = claim_re.search(claim)
        claim_id = int(matches.group(1))
        begin_row = int(matches.group(2))
        begin_col = int(matches.group(3))
        width = int(matches.group(4))
        height = int(matches.group(5))
        for row in range(begin_row, begin_row + width):
            for column in range(begin_col, begin_col + height):
                cell = fabric[row][column]
                no_collision = True
                if cell == 0:
                    fabric[row][column] = claim_id
                else:
                    if cell in non_overlapping:
                        non_overlapping.remove(cell)
                    no_collision = False
                    break
            if not no_collision:
                break
        if no_collision:
            non_overlapping.append(claim_id)

print(non_overlapping)
