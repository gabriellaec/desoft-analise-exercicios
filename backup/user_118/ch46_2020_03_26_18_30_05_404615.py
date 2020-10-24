def numero_no_indice(n):
    n=[]
    n=str(input('diga uma lista:  '))
    i=0
    while i<=len(n) and i==n[i]:
        i+=1
        print (numero_no_indice(n))