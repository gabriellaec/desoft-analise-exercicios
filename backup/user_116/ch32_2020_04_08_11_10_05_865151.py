def lista_primos(n):
    a=0
    lista=[]
    while len(lista)!=n+1:
        if  a == 2:
            lista.append(a)
            a+=1
        elif a == 0 or a == 1:
            a+=1
        elif a%2 == 0:
            a+=1
        else:
            contador = 3
            while contador < a:
                if a%contador == 0:
                    a+=1
                contador += 2    
            lista.append(a)
            a+=1
    return lista