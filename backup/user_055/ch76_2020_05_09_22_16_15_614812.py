def aniversariantes_de_setembro(aniversariantes):
    birth_sept = {}
    datas = aniversariantes.items()
    for aniversariante in datas:
        data = aniversariante[1]
        print(data)
        if data[4] == '9':
            birth_sept[aniversariante[0]] = aniversariante[1]
    return birth_sept