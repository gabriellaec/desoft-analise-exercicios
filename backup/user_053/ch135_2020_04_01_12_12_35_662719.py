# Multiplicando intensidade de pixels

def equaliza_imagem(lista, constante):
    nova_lista = []     # lista de retorno após equalização
    i = 0               # Variável para verificar elemento por elemento da lista

    while i < len(lista):
        x = lista[i]*constante

        if x <= 255:
            nova_lista.append(x)
            i += 1
        else:
            nova_lista.append(255)
            i += 1
    
    return nova_lista

teste = [10, 12, 100]
k = 10
print(equaliza_imagem(teste, k))