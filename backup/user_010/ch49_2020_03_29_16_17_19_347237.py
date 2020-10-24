termos = int(input("Quantos termos terá a sua lista? "))

def inverte_lista (x):

    i=1
    criandolista = True
    lista = [0]*x
    
    while criandolista:
        if i-1==x:
            criandolista = False
        else:
            num=int(input("Digite o {}º número: ".format (i)))
            lista [-i] = num
            i+=1
    return lista

resultado = inverte_lista (termos)
print (resultado)