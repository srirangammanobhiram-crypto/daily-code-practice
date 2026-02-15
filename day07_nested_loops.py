# Day 7 - Nested loops practice

# square star pattern
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

print()

# number pattern
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
