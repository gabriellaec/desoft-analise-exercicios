def is_odd (number):
    return bool(number % 2)

max_n = 0
count = 0

n0 = 0
n = n0

while n0 < 1000:
    counting = 0

    n0 += 1
    n = n0

    while n > 1:
        if is_odd(n):
            n = 3 * n + 1
        else:
            n = n / 2
        
        counting += 1

    if counting > count:
        max_n = n0
        count = counting

print(max_n)