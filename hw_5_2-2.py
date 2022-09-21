# homework 5: dict 2
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

for item in range(len(keys)):
    if keys[item] in sample_dict:
        sample_dict.pop(keys[item])

print(sample_dict)

# Done
