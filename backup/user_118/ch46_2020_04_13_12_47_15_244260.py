def numero_no_indice(n):
    n=[]
    i=int(input('diga uma lista:  '))
    n.append(i)
    while i==n.index:
        i+=1
        print (numero_no_indice(n))