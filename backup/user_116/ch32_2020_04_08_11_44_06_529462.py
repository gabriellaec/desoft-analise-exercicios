def lista_primos(n):
    a=2
    lista=[]
    contador = 3
    while len(lista)!=n:
        if  a == 2:
            lista.append(a)
            a+=1
        elif a%2 == 0:
            a+=1
        elif contador < a :
            contador = 3
            while contador < a:
                if a%contador == 0:
                    contador+=2
                else:
                    lista.append(a)
                    contador=a+2
                    a+=1           
        else:
            a+=1       
    return lista