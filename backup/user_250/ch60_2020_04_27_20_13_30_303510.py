def eh_palindromo(palavra):
    i = 0
    while i < len(palavra)-1:
        if palavra[i] == palavra[:-i]:
            return True
        else:
            return False
        i += 1