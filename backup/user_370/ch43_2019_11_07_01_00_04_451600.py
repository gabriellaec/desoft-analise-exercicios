def Collatz (n):
    i=0
    for i in range(len(n)):
        if i % 2 == 0:
            i= i/2
        else:
            i= 3*i+1
        i+=1
        return len(Collatz)

print ( Collatz(1000))