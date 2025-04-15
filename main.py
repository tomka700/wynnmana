cost, cycle, cycle_cost = [], [], []
# spell cost input
for i in range(4):
    cost.append(float(input(f"{i+1}. spell cost: ")))
# spell cycle input, input to exit cycle isn't counted
spell = 1
j = 1
while 0 < spell < 5:
    spell = int(input(f"{j}. spell: "))
    cycle.append(spell)
    j += 1
cycle.pop()
# sustain and cps input
cps = float(input("cps: "))
mr = float(input("mr: ")) + 25
ms = float(input("ms: "))
# make list of costs and spells
cycle = [[spell, cost[spell - 1]] for spell in cycle]
# shift cost cycle so that first != last
while cycle[0][0] == cycle[-1][0]:
    cycle = [cycle[-1]] + cycle[:-1]
# first two elements are added to avoid out of range error
for i in range(2):
    cycle_cost.append(max(1, cycle[i][1]))
# add amount of repeat times 5 to cost if previous 2 repeated
repeat = 0
for i in range(2, len(cycle)):
    if cycle[i - 1][0] == cycle[i - 2][0]:
        repeat += 1
    else:
        repeat = 0
    cycle_cost.append(max(1, cycle[i][1] + repeat * 5))
# add repeat cost to first if cycle ended with a repeat and if it would go over 1
if (cycle[-1][0] == cycle[-2][0]) and (cycle[0][1] + repeat * 5 > 1):
    cycle_cost[0] += repeat * 5
# sustain - cps * average cost / 3
print("mana / s: {0}".format(mr / 5 + ms / 3 - cps * sum(cycle_cost) / len(cycle_cost) / 3))
