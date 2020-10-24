def make_collatz(start):
    i = 1
    while start != 1:
        if start % 2 == 0:
            start = start/2
        else:
            start = start*3 + 1
        i += 1
    return i

start = 2
collatz = 0
lencollatz = 0

while start < 1000:
    i = make_collatz(start)
    if i > lencollatz:
        collatz = start
        lencollatz = i
    start += 1
print(collatz)
