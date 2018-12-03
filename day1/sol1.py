from itertools import cycle
numlist = []
with open("input.txt") as f:
    for line in f:
        numlist.append(int(line))
print(sum(numlist))

# day 1, puzzle 2
sumlist = set() 
total = 0
for i in cycle(numlist): # infinite cycle of numlist
    total += i
    if total in sumlist:
        print(total)
        break
    sumlist.add(total)

