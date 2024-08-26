


def initialize_items_available():
    return [
        {"name": "Bag of Apples", "weight": 5},
        {"name": "Trail Mix", "weight": 3},
        {"name": "Peanut Butter", "weight": 2},
        {"name": "Bread", "weight": 1},
    ]

def sort_items_by_weight(items_available):
    return sorted(items_available, key=lambda x: x["weight"], reverse=True)

def add_initial_items(bag_capacity, items_available):
    backpack = []
    for item in items_available:
        backpack.append({"item": item["name"], "count": 1})
        bag_capacity -= item["weight"]
    return backpack, bag_capacity

def fill_remaining_capacity(bag_capacity, items_available, backpack):
    for item in items_available:
        while bag_capacity >= item["weight"]:
            for packed_item in backpack:
                if packed_item["item"] == item["name"]:
                    packed_item["count"] += 1
                    break
            bag_capacity -= item["weight"]
    return backpack



def pack_food_backpack(bag_capacity):
    items_available = initialize_items_available()
    items_available = sort_items_by_weight(items_available)
    backpack, remaining_capacity = add_initial_items(bag_capacity, items_available)
    backpack = fill_remaining_capacity(remaining_capacity, items_available, backpack)
    return backpack

# Test cases
print(pack_food_backpack(27))  # Input Bag Capacity: 27
print(pack_food_backpack(38))  # Input Bag Capacity: 38
print(pack_food_backpack(15))  # Input Bag Capacity: 15


# In[ ]:




