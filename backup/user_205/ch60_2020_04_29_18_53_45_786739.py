# Método com fatiamento
def eh_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
# Método sem fatiamento  
def eh_palindromo(palavra):
    for i in palavra:
        teste = palavra.replace(palavra[0],palavra[-1])
    if teste == palavra:
        return True 
    else:
        return False