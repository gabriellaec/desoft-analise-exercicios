def make_collatz(start):
    count = 1
    
    while start != 1:
        if start % 2 == 0:
            start = start/2
        else:
            start = start*3 + 1
        
        count = count + 1
    
    return count

start = 2
collatz = 0
lencollatz = 0

while start < 1000:
    i = make_collatz(start)
    
    if i > lencollatz:
        collatz = start
        lencollatz = i
    
    start = start + 1

print(collatz)