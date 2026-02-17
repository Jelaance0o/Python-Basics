# enumerate()

users = ["Jeelance", "Rahul", "Aman"]

for index, user in enumerate(users, start=1):
    print(index, user)


# Dictionary loop

user = {
    "name": "Jeelance",
    "age": 21,
    "role": "Developer"
}

for key, value in user.items():
    print(f"{key}: {value}")


# Nested loop

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    for j in numbers:
        if i != j and i + j == 6:
            print(i, j)


# Break and continue

for i in range(1, 11):
    if i == 3:
        continue

    if i == 8:
        break

    print(i)


# List comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(squares)