palavra=input(' escreva uma palavra')
def lista_caracteres(palavra):
    letras=[]
    for i in palavra:
        if i not in letras:
            letras.append(i)
    return lista
        