# homework 5: loops 1

numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item % 5 == 0:
        if item > 500:
            break
        elif item > 150:
            continue
        print(item)

# Done
