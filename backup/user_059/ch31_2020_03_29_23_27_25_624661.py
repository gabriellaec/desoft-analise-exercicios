def eh_primo(x):
    i = 3
    while i<x:
        y = x%2
        w = x%i
        i+=2
        if y==0 or w ==0:
            return False  
        else:
            return True

print(eh_primo(52))