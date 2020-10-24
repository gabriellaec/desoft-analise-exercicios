def eh_palindromo(lista):
    i= 1
    lista_invertida= []
    while i <= len(lista):
        lista_invertida.append(lista[-i])
        i = i + 1
    print(lista_invertida)
    x= 0
    while x < len(lista_invertida):
        if lista_invertida[x]== lista[x]:
            return True
            x= x + 1
        else:
            return False
