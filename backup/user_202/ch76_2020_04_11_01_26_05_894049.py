def aniversariantes_de_setembro(niver):
    dic = {}
    for k,v in niver.items():
        mes = []
        c = 0
        for i in v:
            c += 1
            if c == 4 or c == 5:
                mes.append(i)
        if mes[0] == 0 and mes[1] == 9:
            dic[k] = v
    return dic
        
                
                
                
        