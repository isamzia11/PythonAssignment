# Name Isam Zia Roll no: TRN-2026-00346 


def countdown(n):
    while n >= 0:
        yield n
        n -= 1


def evens(limit):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number


print("===== COUNTDOWN =====")
for number in countdown(5):
    print(number)

print("===== EVEN NUMBERS =====")
print(list(evens(10)))
