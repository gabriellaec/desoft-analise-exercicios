def encontra_maximo(m):
   maior = abs(m[0][0]) 
   for i in range (0,len(m)):
    for j in range(len(abs(m[i]))):
        if abs(m[i][j]) > maior:
            maior = abs(m[i][j])
   return maior