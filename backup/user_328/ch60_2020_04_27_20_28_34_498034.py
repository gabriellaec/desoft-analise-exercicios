#desafio 1
def eh_palindromo(string):
    return string == string[::-1]

#desafio 2
def eh_palindromo(string):
    palindromo = True
    i= 0
    j= len(string)-1
    while i < j:
        if string[i] != string[j]:
            palindromo = False
        i += 1
        j -= 1
    return palindromo