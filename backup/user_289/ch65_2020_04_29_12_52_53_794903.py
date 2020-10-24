def capitaliza(palavra):
    string = str(palavra)
    primeira_letra = string[0].upper()
    restante = string[1::]
    palavra_capitalizada = primeira_letra + restante
    return palavra_capitalizada