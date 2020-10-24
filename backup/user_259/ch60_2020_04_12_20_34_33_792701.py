def eh_palindromo(palavra):
    i = 0
    while i<len(string):
        if palavra[i] == palavra[-i]:
            i+=1
        else:
            return False
    return True