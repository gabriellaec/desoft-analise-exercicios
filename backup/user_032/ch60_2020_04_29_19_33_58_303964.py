def eh_palindromo(palavra):
    for i in palavra:
        for x in palavra[::-1]:
            if i == x:
                return True
            else:
                return False