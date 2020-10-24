def eh_par_ou_impar(x):
    if x%2==0:
        if x==0:
            return 1
        return x/2
    else:
        return 3*x+1

def collatzinho(numero):
    lista=[numero]
    while True:
        a = eh_par_ou_impar(numero)
        lista.append(a)
        if a==1:
            break
        numero=a
    return len(lista)
tamanho = []
i=0
while i<1000:
    tamanho.append(collatizinho(i))
    i+=1
    
print(tamanho.index(max(tamanho)))
    
