# Day 11 - Lists basics

numbers = [10, 20, 30, 40, 50]

# access elements
print(numbers[0])
print(numbers[-1])

# change value
numbers[1] = 99
print(numbers)

# length
print("Length:", len(numbers))

# loop through list
for num in numbers:
    print("Value:", num)
