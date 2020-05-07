import random

dem_sup_count = random.randint(5, 10)

demand = []
supply = []
costs = []
nwc = []

for i in range(dem_sup_count):
    demand.append(random.randint(200, 500))

supply = demand.copy()
supply.reverse()

for i in range(dem_sup_count):
    temp = []
    t = []
    for j in range(dem_sup_count):
        temp.append(random.randint(5, 55))
        t.append(0)
    costs.append(temp)
    nwc.append(t)

i = 0  # tracking supply
j = 0  # tracking demand
while (i != dem_sup_count or j != dem_sup_count):
    x = 0
    if (supply[i] < demand[j]):
        x = supply[i]
    else:
        x = demand[j]
    supply[i] -= x
    demand[j] -= x
    nwc[i][j] = x
    if (supply[i] == 0 and i < dem_sup_count):
        i += 1
    if (demand[j] == 0 and j < dem_sup_count):
        j += 1

total_cost = 0
for i in range(dem_sup_count):
    for j in range(dem_sup_count):
        total_cost += nwc[i][j] * costs[i][j]

print("Total cost =", total_cost)