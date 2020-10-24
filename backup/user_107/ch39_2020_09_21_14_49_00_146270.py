def is_odd (number):
    return bool(number % 2)

n_0 = 1000
n = n_0

while n != 1:
    n_0 -= 1
    n = n_0

    while n > 1:
        if is_odd(n):
            n = 3 * n + 1
        else:
            n = n / 2

print(n_0)