# Example dictionary
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict["c"] = [1, 2, 3]
print(dict)

# Example dictionary
dict_2 = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict_2[key] += 1
print(dict_2)

# Which line of code will print "Steak"?
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])