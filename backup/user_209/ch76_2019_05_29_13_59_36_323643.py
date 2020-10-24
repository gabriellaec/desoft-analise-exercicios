def aniversariantes_de_setembro (dic):
    dicnobas = {}
    for nomes,data in dic.items():
            if "0" == data[4] and "9" == data[5]:
                dicnobas[nomes] = data
        return dicnobas
               
                