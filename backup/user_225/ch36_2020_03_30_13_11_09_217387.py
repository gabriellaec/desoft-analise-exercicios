def fatorial(n):
    resultado =1
    count = 1
    if n == 0 or n==1:
        resultado == 1
    while count <= n:
        resultado*=count
        count+=1
    print(resultado)