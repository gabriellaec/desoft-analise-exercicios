def lista_sufixos(frase):
    lista = []
    contador = len(frase) - 1
    soma = ""
    while contador >= 0 :
        soma += frase[contador]
        lista.append(soma[::-1])
        contador -= 1
    return lista