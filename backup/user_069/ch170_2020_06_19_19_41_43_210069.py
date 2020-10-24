def apaga_repetidos(palavra):

    lista_letras = []
    palavra_final = ""

    for letra in palavra:

        if letra in lista_letras:
            palavra_final += '*'
            
        else:
            palavra_final += letra
            lista_letras.append(letra) 

    return palavra_final