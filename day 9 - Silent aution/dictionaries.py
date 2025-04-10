programming_terms = {
    "Bug": "An error in the code that causes it to work incorrectly.",
    "Function": "A reusable block of code that performs a specific task.",
    "Loop": "A way to repeat a block of code multiple times."
}
# This is how we reference the value of the one of the keys in the dictionary
print(programming_terms["Bug"])

# How to append further key value pairs to a dictionary?
programming_terms["Dictionary"] = "Data structure that stores data in key-value pairs"
print(programming_terms)


# Empty list
empty_list = []

# Empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_terms = {}
print(programming_terms)

# Edit an item in a dictionary
programming_terms["Bug"] = "An error in the system that causes it to work incorrectly"
print(programming_terms)

# Loop through a dictionary
for key in programming_terms:
    print(key)
    print(programming_terms[key])


