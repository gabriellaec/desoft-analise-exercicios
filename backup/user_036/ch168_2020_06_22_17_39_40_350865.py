def login_disponivel(nome, lista):
    qtde = 0
    for n in lista:
        if nome in n:
            qtde += 1
    return nome if qtde == 0 else f'{nome}{qtde}'