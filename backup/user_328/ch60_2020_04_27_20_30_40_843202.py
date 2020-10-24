#desafio 1
def eh_palindromo(string):
    return string == string[::-1]

#desafio 2
def eh_palindromo(string):
    palindromo = True
    i= 0 #conta as letras na ordem normal
    j= len(string)-1 #conta as letras de trás para frente
    while i < j:
        if string[i] != string[j]: #os dois contadores tem que ter o mesmo indice
            palindromo = False
        i += 1
        j -= 1
    return palindromo