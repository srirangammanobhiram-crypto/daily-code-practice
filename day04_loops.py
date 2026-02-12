# Day 4 - Loops Practice

# 1️⃣ Print numbers 1 to 10
for i in range(1, 11):
    print(i)


# 2️⃣ Print even numbers between 1 and 20
for i in range(1, 21):
    if i % 2 == 0:
        print("Even:", i)


# 3️⃣ Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i

print("Sum is:", total)


# 4️⃣ While loop example
num = 1
while num <= 5:
    print("Count:", num)
    num += 1
