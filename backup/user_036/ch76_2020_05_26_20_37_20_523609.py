def aniversariantes_de_setembro(teste):
    s = dict()
    for i in teste:
        if teste[i][3] == '0' and teste[i][4] == '9':
            s[i] = teste[i]
            print(s)