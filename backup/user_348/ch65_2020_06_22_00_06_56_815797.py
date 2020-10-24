def capitaliza (string):
    # Cria uma variável com tudo da string menos a primeira letra
    resto = string[1:]
    # Cria uma variável com a primeira letra da string
    primeira_letra = string[0]
    # Cria uma variável com a primeira letra em maiúscula
    captaliza = primeira_letra.upper()
    # Soma a primeira letra em maiúscula com o resto
    soma = captaliza + resto
    return soma

print(capitaliza ('Thais'))