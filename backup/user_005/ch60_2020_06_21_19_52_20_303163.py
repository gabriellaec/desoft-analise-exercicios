def eh_palindromo(palavra):
    palavra = input('escreva algo:')
    if palavra != palavra[::-1]:
        return True
    else:
        return False