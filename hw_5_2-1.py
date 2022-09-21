# homework 5: dict 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = {}

for my_key in keys:
    for my_value in values:
        my_dict[my_key] = my_value
        values.remove(my_value)
        break
print(my_dict)

# Done
