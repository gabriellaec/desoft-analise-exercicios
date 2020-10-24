def filtra_positivos(numeros):
   lista=[]
   i=0
   while i < len(numeros):
        if numeros[i] > 0:
            lista.append(numeros[i])
        i+=1
   return lista
numeros=[1,2,-8,-7,-2,0]
print(filtra_positivos(numeros))
