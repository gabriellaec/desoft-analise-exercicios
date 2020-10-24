def aniversariantes_de_setembro (dic):
    dicnobas = {}
    for nomes,data in dic.items():
        for e in range(len(dic[data])):
            if "0" == e[4] and "9" == e[5]:
                dicnobas[nomes] = data
        return dicnobas
               
                