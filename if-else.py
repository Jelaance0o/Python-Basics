age = 23

if age >= 18:
    print("Adult")
else:
    print("Minor")


# elif------

marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Condition using AND---------------------

    age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Using OR operater----------- one must be true

has_ticket = False
is_vip = True

if has_ticket or is_vip:
    print("Entry allowed")
else:
    print("Entry denied")


# NOT operater

is_logged_in = False

if not is_logged_in:
    print("Please login")
else:
    print("Welcome")


# Nested if else

age = 25
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed")
    else:
        print("ID required")

else:
    print("You must be 18 or older")