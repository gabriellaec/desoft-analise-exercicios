def apaga_repetidos(string):
    lista_letras = []
    string_final = ''
    for letra in string:
        LETRA = letra.upper()
        if LETRA not in lista_letras:
            lista_letras.append(LETRA)
            string_final += letra
        else:
            string_final += '*'
    return string_final        


    