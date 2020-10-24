def calcula_fibonacci(n):
    lista_fibo = []
    

    if n == 0:
        lista_fibo=[]
    elif n==1: 
        valor1 = 1
        lista_fibo.append(valor1)
    elif n==2:
        valor1 = 1
        valor2 = 1
        lista_fibo.append(valor1)
        lista_fibo.append(valor2)
    else:
        valor1 = 1
        valor2 = 1
        lista_fibo.append(valor1)
        lista_fibo.append(valor2)
        i = 2
        while len(lista_fibo) < n:
            novo = lista_fibo[i-1] + lista_fibo[i-2]
            lista_fibo.append(novo)
            i+=1
        return lista_fibo
        
    