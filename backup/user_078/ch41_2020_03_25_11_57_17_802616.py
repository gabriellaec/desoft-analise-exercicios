valores=[10, -4, 9, 0, -3, 4]
print (valores)
def zera_negativos(valores):
    i=0
    while i>len(valores):
        if valores[i]<0:
            valores[i]=0
        i=i+1
