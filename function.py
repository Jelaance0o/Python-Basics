def greet():
    print("Hello, welcome to Python!")

greet()
# --------------------

def add(a, b):
    return a + b;

result = add(10, 20)

print(result)

# Type hints -------------------------

def product(a:int , b:int )->int:
    return a*b

pro = product(10,20)

print(pro)

# -----------------------------------

def greet(name="User"):
    print("Hello", name)

greet()
greet("Jeelance")

# Higher order function || fucntion as an argument

def calculate(a, b, operation):
    return operation(a, b)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(calculate(10, 5, add))
print(calculate(10, 5, multiply))


