vet=[3,4]
def calcula_norma(vet):
    i=0
    soma=[]
    while i!=len(vet):
        sm = vet[i]**2
        soma.append(sm)
        i+=1
    modulo = (sum(soma))**(1/2)
    return modulo
        
print(calcula_norma(vet))
print(vet)    