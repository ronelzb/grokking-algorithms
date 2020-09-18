def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if node not in visited and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra(start):
    costs = {}
    parents = {}

    for key in graph[start]:
        costs[key] = graph[start][key]
        parents[key] = start

    node = find_lowest_cost_node(costs)

    while node:
        cost = costs[node]
        neighbors = graph[node]

        for neighbor in neighbors:
            new_cost = cost + neighbors[neighbor]

            if neighbor not in costs or costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        visited.add(node)
        node = find_lowest_cost_node(costs)

    print(costs)
    return parents


# graph = {"start": {"a": 6, "b": 2}, "a": {"end": 1}, "b": {"a": 3, "end": 5}, "end": {}}
graph = {"start": {"a": 5, "b": 2}, "a": {"c": 4, "d": 2}, "b": {"a": 8, "d": 7}, "c": {"end": 3, "d": 6},
         "d": {"end": 1}, "end": {}}
visited = set()

print(dijkstra("start"))
