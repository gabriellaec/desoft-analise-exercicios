def capitaliza(palavra):
    letra=palavra[0]
    maiu=letra.upper()
    palavra=palavra.replace(letra, maiu)
    return palavra