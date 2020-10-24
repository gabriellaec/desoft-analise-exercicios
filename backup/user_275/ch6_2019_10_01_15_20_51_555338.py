def encontra_maximo(m):
   maior = m[0][0] 
   for i in range (0,len(m)):
    for j in range(len(m[i])):
        if m[i][j] > maior:
            maior = m[i][j]
   return maior