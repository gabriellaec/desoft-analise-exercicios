def encontra_maximo(m):
   maior=m[0]
   for i in m:
        if m[i]>maior:
            maior=i
        return maior