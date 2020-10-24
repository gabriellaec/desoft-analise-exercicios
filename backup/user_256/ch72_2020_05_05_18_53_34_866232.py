def lista_caracteres(palavra):
    q = []
    for letras in palavra:
        if not letras in q:
            q = letras.split(',')
    print(q)
    return q
        








