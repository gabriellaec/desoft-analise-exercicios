def eh_palindromo(palavra):
    palidromo = True
    i = 0
    j = len(palavra) - 1
    while i > j:
        if palavra[i] != palavra[j]:
            palindromo = False
    i += 1
    j -= 1
    return palindromo
    