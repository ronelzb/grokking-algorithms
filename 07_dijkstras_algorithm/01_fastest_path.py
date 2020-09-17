def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if node not in visited and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def fastest_path(start):
    costs = {}
    parents = {}

    # initialize costs and parents
    for key in graph[start].keys():
        costs[key] = graph[start][key]
        parents[key] = start

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if n not in costs or costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        visited.add(node)
        node = find_lowest_cost_node(costs)

    print(costs)
    return parents


graph = {"start": {"a": 6, "b": 2}, "a": {"end": 1}, "b": {"a": 3, "end": 5}, "end": {}}
visited = set()
print(fastest_path("start"))
