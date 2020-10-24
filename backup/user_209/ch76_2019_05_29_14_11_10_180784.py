def aniversariantes_de_setembro (dic):
    dicnobas = {}
    for nomes,data in dic.items():
        if data[3]=='0' and data[4]=='9':
            dicnobas[nomes]=data
    return dicnobas
               
                