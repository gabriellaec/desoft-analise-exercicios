def captaliza (string):
    primeira_letra = string[0]
    captaliza = string.upper(primeira_letra)
    resto = string[1:]
    soma = captaliza + resto
    return soma