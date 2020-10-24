def cria_bigramas(T):
    bigramas=[]
    i=0
    n=len(T)-1
    while i<n:
        B=T[i]+T[i+1]
        bigramas.append(B)
        i+=1
    return bigramas
ex="babador"
print(cria_bigramas(ex))
def acha_bigramas(ex):
   lista_final=[]
   i=0
   B=cria_bigramas(ex)
   n=len(B)
   while i<n:
       if B[i] not in lista_final:
           lista_final.append(B[i])
           
       i+=1
   return lista_final