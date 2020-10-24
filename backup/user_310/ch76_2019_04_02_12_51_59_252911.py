def aniversariantes_de_setembro(d):
    aniversariantes={}
    
    for pessoa in d:
        if d[pessoa][3:5]=="09":
            aniversariantes["pessoa"]=aniversariantes[pessoa]
    return aniversariantes