def eh_palindromo(string):
    palindromo= True
    i = 0
    j = len(string)-1
    while i < j:
        if string[i] == string[j]:
            palindromo = False
        i+=1
        j+=1
    return palindromo
print(verifica_palindromo('roma é amor'))
print(verifica_palindromo('Insper'))

