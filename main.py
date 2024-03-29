cost, cycle, cycle_cost = [], [], []
j = 1
spell = 1
repeat = 0
# spell cost input
for i in range(4):
    cost.append(float(input("{0}. spell cost: ".format(i + 1))))
# spell cycle input, input to exit cycle isn't counted
while 0 < spell < 5:
    spell = int(input("{0}. spell: ".format(j)))
    cycle.append(spell)
    j += 1
cycle.pop()
# sustain and cps input
cps = float(input("cps: "))
mr = float(input("mr: ")) + 25
ms = float(input("ms: "))
# make list of costs and spells
for i in range(len(cycle)):
    for j in range(4):
        if cycle[i] == j + 1:
            cycle[i] = [cost[j], j + 1]
# shift cost cycle so that first != last
while cycle[0][1] == cycle[-1][1]:
    cycle = [cycle[-1]] + cycle[:-1]
# first two elements are added to avoid out of range error
for i in range(2):
    if cycle[i][0] <= 1:
        cycle_cost.append(1)
    else:
        cycle_cost.append(cycle[i][0])
# add amount of repeat times 5 to cost if previous 2 repeated
for i in range(2, len(cycle)):
    if cycle[i - 1][1] == cycle[i - 2][1]:
        repeat += 1
        if cycle[i][0] + repeat * 5 <= 1:
            cycle_cost[i].append(1)
        else:
            cycle_cost.append(cycle[i][0] + repeat * 5)
    else:
        repeat = 0
        if cycle[i][0] <= 1:
            cycle_cost[i].append(1)
        else:
            cycle_cost.append(cycle[i][0])
# add repeat cost to first if cycle ended with a repeat and if it would go over 1
if (cycle[-1][1] == cycle[-2][1]) & (cycle[0][0] + repeat * 5 > 1):
    cycle_cost[0] += repeat * 5
# sustain - cps * average cost / 3
print("mana / s: {0}".format(mr / 5 + ms / 3 - cps * sum(cycle_cost) / len(cycle_cost) / 3))
