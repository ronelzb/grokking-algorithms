def dynamic_programming(goods, max_items):
    arr = [[{"max_value": 0, "items": set()} for j in range(max_items)] for i in range(len(goods))]

    for i in range(len(goods)):
        current_weight = goods[i]["weight"]

        for j in range(max_items):
            current_value = goods[i]["cost"] if current_weight <= j + 1 else 0
            previous_max = arr[i - 1][j]["max_value"] if i > 0 else 0
            remaining_space_value = arr[i - 1][j - current_weight]["max_value"] if j > current_weight else 0
            remaining_space_items = arr[i - 1][j - current_weight]["items"] if j > current_weight else set()

            if previous_max < current_value + remaining_space_value:
                arr[i][j] = {"max_value": current_value + remaining_space_value,
                             "items": {goods[i]["name"]} | remaining_space_items}
            else:
                arr[i][j] = arr[i - 1][j]

    return arr[len(goods) - 1][max_items - 1]


items = [{"name": "guitar", "weight": 1, "cost": 1500},
         {"name": "stereo", "weight": 4, "cost": 3000},
         {"name": "laptop", "weight": 3, "cost": 2000},
         {"name": "iphone", "weight": 1, "cost": 2000},
         {"name": "mp3", "weight": 1, "cost": 1000}]

# items2 = {"water": {"lb": 3, "relevance": 10}, "book": {"lb": 1, "relevance": 3}, "food": {"lb": 2, "relevance": 9},
#           "jacket": {"lb": 2, "relevance": 5}, "camera": {"lb": 1, "relevance": 6}}

print(dynamic_programming(items, 4))
