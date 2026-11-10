
import math


def area_of_circle(r):
    area = math.pi * r ** 2
    return area


def is_even(n):
    return n % 2 == 0


def greet(name, lang="en"):
    if lang == "ur":
        return f"Salaam, {name}!"

    return f"Hello, {name}!"


print("===== CIRCLE AREAS =====")
print(area_of_circle(2))
print(area_of_circle(5))
print(area_of_circle(10))

print("\n===== EVEN OR ODD =====")
print(is_even(8))
print(is_even(7))
print(is_even(20))

print("\n===== GREETINGS =====")
print(greet("Ali"))
print(greet("Sara", "ur"))
print(greet("Ahmed", "en"))
