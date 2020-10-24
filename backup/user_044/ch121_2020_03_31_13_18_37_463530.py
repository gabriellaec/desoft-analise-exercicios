def subtracao_de_listas(lista1,lista2):
    ls=[]
    i=0
    n=len(lista1)
    j=0
    m=len(lista2)
    if n>=i:   
        while i<=n:
            if m>=j:
                while j<=m:
                    if lista1[i]==lista2[j]:
                        ls.append(lista1[i])
                        j+=1
                    else:
                        j+=1
                i+=1
    else:
        ls=[]
    return ls
            