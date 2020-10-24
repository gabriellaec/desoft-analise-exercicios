def subtracao_de_listas(lista1,lista2):
    ls=[]
    n=len(lista1)
    i=0
    p=len(lista2)
    while i<=n:
        lista1[i]=str(lista1[i])
        i+=1
    i=0
    while i<=p:
        lista2[i]=str(lista2[i])
        i+=1    
    i=0
    if lista1[i] in 