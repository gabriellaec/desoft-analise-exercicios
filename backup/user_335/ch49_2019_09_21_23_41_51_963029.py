def CriadorLista():
    lista = []
    v = int(input("Digite um número: "))
    lista.append(v)

    while v>0:
        v = int(input("Digite um número: "))
        lista.append(v)  
    return lista

def Inversor(lista):
    invertida = []
    i = 1
    while i <= len(lista):
        invertida.append(lista[-i])
        i += 1  
    return invertida

lista = CriadorLista()
listainvertida = Inversor(lista)
print (listainvertida)