# Método com fatiamento
def eh_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
    
# Método sem fatiamento  
def eh_palindromo(palavra):
    lista = []
    lista2 = []
    for i in palavra:
        lista.append(i)
    for j in reversed(lista):
        lista2.append(j)
    if lista == lista2:
        return True
    else:
        return False  