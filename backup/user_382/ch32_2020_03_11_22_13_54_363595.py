def lista_primos(n):
    lista = [0]*n
    div = 3
    num = 2
    t = 0 
    while num <= n: 
        if num % 2 ==0 and num!=2 or num ==1 or num == 0:
            x = False 

        while num > div:
            if num % div == 0:
                x = False 
                div +=2
        x = True 
        if x == True:
            lista[t] = num
            num += 1
            t +=1
    print(lista_primos)