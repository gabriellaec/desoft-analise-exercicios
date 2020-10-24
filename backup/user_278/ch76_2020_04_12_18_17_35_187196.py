def aniversariantes_de_setembro(nomes):
    niver_setembro = {}
    nomes_data = nomes.values()
    i=0
    for k,v in nomes.items():
        if v[3]=="0" and v[4]=="9":
            niver_setembro[k] = v
            i+=1
    return niver_setembro