def eh_palindromo(palavra):
    inverso = palavra[::-1]
    vdd = inverso == palavra
    if vdd:
        return vdd
    