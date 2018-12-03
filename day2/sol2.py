from itertools import combinations
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# We'll use this to compare each box id against each other one
ids = []
with open("input.txt") as f:
    for box_id in f:
        ids.append(box_id)

for id_1, id_2 in combinations(ids, 2):
    differences = sum([letter1 != letter2 for letter1, letter2 in zip(id_1, id_2)])
    if differences == 1:
        print("".join([letter1 for letter1, letter2 in zip(id_1, id_2) if letter1 == letter2]))
        break
