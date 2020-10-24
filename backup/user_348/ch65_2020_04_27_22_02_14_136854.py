def capitaliza (string):
    resto = string[1:]
    primeira_letra = string[0]
    captaliza = primeira_letra.upper()
    soma = captaliza + resto
    return soma

print(capitaliza ('Thais'))