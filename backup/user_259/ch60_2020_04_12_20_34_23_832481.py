def eh_palindromo(palavra):
    while i<len(string):
        if palavra[i] == palavra[-i]:
            i+=1
        else:
            return False
    return True