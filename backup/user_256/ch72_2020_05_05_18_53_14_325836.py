def lista_caracteres(palavra):
    q = []
    for letras in palavra:
        if not letras in q:
            q = palavra.split(',')
    print(q)
    return q
        








