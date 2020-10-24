def make_collatz(start):
    result = []
    
    while start != 1:
        if start % 2 == 0:
            start = start/2
        else:
            start = start*3 + 1
            
    return len(result)

start = 4
collatz = 3

while start < 1000:
    if make_collatz(collatz) < make_collatz(start):
        collatz = start

print(collatz)