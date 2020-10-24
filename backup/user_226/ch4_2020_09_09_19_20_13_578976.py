def classifica_idade(idade):
    if 0 < idade <= 11:
        print("crianca")
    elif 12 <= idade <= 17:
        print('adolescente')
    else:
        print("adulto")