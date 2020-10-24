def aniversariantes_de_setembro(dicionario):
    ani_setembro = {}
    for n,i in dicionario.items():
        #print(i)
        # data = i.split("/")
        if i[3] == "0" and i[4] == "9":
            ani_setembro[n] = i
    return ani_setembro