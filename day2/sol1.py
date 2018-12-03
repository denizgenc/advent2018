ids = []
with open("input.txt") as f:
    for box_id in f:
        ids.append(box_id)

double_count, triple_count = 0, 0
for box_id in ids:
    uniques = set(box_id)
    found_double = False
    found_triple = False
    for letter in uniques:
        if box_id.count(letter) == 2 and not found_double:
            double_count += 1
            found_double = True
        elif box_id.count(letter) == 3 and not found_triple:
            triple_count += 1
            found_triple = True

        if found_double and found_triple:
            break

print(double_count * triple_count)

