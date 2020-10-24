def apaga_repetidos(letras):
    dicionario_letras= {}
    novas_letras= ""
    for letra in letras:
        if letra in dicionario_letras:
            novas_letras += '*'
        else:
            novas_letras += letra
            dicionario_letras[letra] = letra
    return novas_letras

#banana= 'banana'
#print(apaga_repetidos(banana))
#             OU 
def apaga_repetidos(letras):
    lista_letras= []
    novas_letras= ""
    for letra in letras:
        if letra in lista_letras:
            novas_letras += '*'
        else:
            novas_letras += letra
            lista_letras.append(letra)
    return novas_letras