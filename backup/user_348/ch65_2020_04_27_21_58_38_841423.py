def capitaliza (string):
    resto = string[1:]
    primeira_letra = string[0]
    captaliza = string.upper(primeira_letra)
    soma = captaliza + resto
    return soma

print(capitaliza ('Thais'))