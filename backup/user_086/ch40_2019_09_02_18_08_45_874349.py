def fatorial(n):
    controle=0
    fatnum=1
    #n-1*n-2*n-3*...*n-n
    while controle<n:
        fatnum=(n-controle)*fatnum
        controle+=1
    return fatnum
print(fatorial(4))
        