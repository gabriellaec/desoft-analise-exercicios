def eh_palindromo(string):
    x = True
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            x = False
            break
    return x