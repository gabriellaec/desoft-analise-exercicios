def verifica_lista(l):
    categoria = []
    for num in l:
        if num % 2 == 0:
            categoria.append('par')
        else:
            categoria.append('impar')
    if 'impar' not in categoria and 'par' in categoria:
        return 'par'
    elif 'impar' in categoria and not 'par' in categoria:
        return 'impar'
    else:
        return 'misturado'