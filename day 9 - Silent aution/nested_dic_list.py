capitals = {
    "Colombia": "Bogota",
    "Italy": "Rome"
}

# Nested list in a Dictionary

travel_log = {
    "Colombia": ["Cali", "Armenia", "Manizales", "Bello", "Pereira"],
    "Germany": ["Berlin", "Stuttgart"]
}

# print Armenia
print(travel_log["Colombia"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0])

# Nested Dictionaries
travel_log_v2 = {
    "France": {
        "total_visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    "Colombia": {
        "total_visits": 4,
        "cities": ["Cali", "Armenia", "Palmira"]
    }
}

print(travel_log_v2["Colombia"]["cities"][2])