lista = []
def collatz(x):
    lista.append(x)
    while x<1000:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
            