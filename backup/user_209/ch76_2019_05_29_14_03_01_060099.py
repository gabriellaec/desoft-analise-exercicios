def aniversariantes_de_setembro (dic):
    dicnobas = {}
    for nomes,data in dic.items():
        if data[4]=='0' and data[5]=='9':
            dicnobas[nomes]=data
    return dicnobas
               
                