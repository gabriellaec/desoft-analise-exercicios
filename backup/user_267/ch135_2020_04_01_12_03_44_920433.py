lista_intensidades =[10,20,30]
lista_nova = []
def equaliza_imagem(lista_intensidades,k):
    quantia_termos = len(lista_intensidades)
    termo = 0
    while termo < quantia_termos:
        for i in lista_intensidades:
            i = i*k
            termo += 1
            if i > 255:
                i = 255
                lista_nova.append(i)
            else:
                lista_nova.append(i)
            print(lista_nova)
    