contador = 1

def fatorial(x):
    while x+1<=contador :
        x = x * contador
        contador = contador +1
        return x
    else: 
        print (x)