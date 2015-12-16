
num_cities = int(raw_input("Number of cities:"))

city_costs = []
city_places = []

for i in range(num_cities):
    print "City #{}".format(i+1)
    city_costs.append(int(raw_input("Cost of entering:")))
    city_places.append(
        map(int, raw_input("Cost of each place in the city:").split())
    )
    city_places[i].sort()
    city_places[i] = reduce(
        lambda a, c: a + [c+a[-1]], city_places[i], city_costs[i:i+1]
    )
    city_places[i][0] = 0


money_possiblities = [{int(raw_input("Starting money:")): (0, -1)}]


def calc_posiblities(last_posibles, costs):
    result = {}
    for money, (visited, _) in last_posibles.items():
        for nplaces, cost in enumerate(costs):
            if cost > money:
                break

            rem = money - cost
            if rem not in result:
                result[rem] = (nplaces + visited, money)
            else:
                new_visited = visited + nplaces
                last_visited = result[rem][0]
                if new_visited > last_visited:
                    result[rem] = (new_visited, money)

    return result


for costs in city_places:
    last_posibles = money_possiblities[-1]
    new_posibles = calc_posiblities(last_posibles, costs)
    money_possiblities.append(new_posibles)


def find_best(moneys):
    best_money = moneys.keys()[0]
    for money, (places, _) in moneys.items():
        if places > moneys[best_money][0]:
            best_money = money
    return best_money


def form_answer(end_money):
    result = [[end_money, 0]]
    next_money = end_money
    for moneys in reversed(money_possiblities):
        result[-1][1], next_money = moneys[next_money]
        result.append([next_money, 0])
    return result[:-1]


last_step = money_possiblities[-1]
best_result = find_best(last_step)
answer = form_answer(best_result)

print "It is possible to visit {} places.".format(answer[0][1])
print "Steps are as follows:"
for ans in reversed(answer):
    print ans
