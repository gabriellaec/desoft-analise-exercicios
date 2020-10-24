def lista_primos(n):
    n = int(input('Insira o numero de termos:'))
    t = 0 
    num = 2 
    lista = [0]*n
    while n > t:
        div = 2 
        while num >= div:
            if num % 0 == 0:
                break 
            else:
                div += 1
        if num == div:
            lista[t] = num 
            t+=1
        num += 1 
    return lista 