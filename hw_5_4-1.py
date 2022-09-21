# homework 5: Tuple 1

tuple1 = (10, 20, 30, 40, 50)

new_tuple = ()

for item in tuple1:
    new_tuple = (item,) + new_tuple

print(new_tuple)

# Done
