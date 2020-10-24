valores=[-7,9,13,-11,5]

def zera_negativos(valores):
    i=0
    while i<len(valores):
    if valores[i]<0:
        return valores[i]=0
    i+=1
print(valores)