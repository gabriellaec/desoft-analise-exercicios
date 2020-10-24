def capitaliza(palavra):
    x = palavra[1:]
    y = palavra[0].upper()
    z = y+x
    return z
print(capitaliza('vitor'))