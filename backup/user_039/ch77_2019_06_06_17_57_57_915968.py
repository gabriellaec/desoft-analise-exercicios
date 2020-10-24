def calcula_tempo(dict):
    dictnovo={}
    for string,a in dict.items():
        dictnovo[string]=(200/a)**(1/2)
    return dictnovo


