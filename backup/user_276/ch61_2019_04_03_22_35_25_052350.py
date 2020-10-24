def eh_palindromo(palavra):
    palidromo = True
    i = 0
    j = len(palavra) - 1
    while i > j:
        if palavra[i] != palavra[j]:
            palindromo = False
    return palindromo
    