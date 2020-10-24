def eh_palindromo(palavra):
    i = 0
    I = len(palavra-1)
    while i < len(palavra)-1:
        if palavra[i] == palavra[:-I]:
            return True
        else:
            return False
        i += 1