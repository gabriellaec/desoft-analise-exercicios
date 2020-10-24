def eh_palindromo(lista):
    i= 1
    lista_invertida= ''
    while i <= len(lista):
        lista_invertida= lista_invertida + lista[-i]
        i = i + 1
    print(lista_invertida)
    if lista_invertida== lista:
        return True
    else:
        return False
