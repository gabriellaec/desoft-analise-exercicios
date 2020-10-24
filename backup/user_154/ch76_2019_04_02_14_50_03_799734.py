def aniversariantes_de_setembro(dic):
    result = {}
    
    for name, date in dic.itens():
        if date.split("/")[1] == "09":
            result[name] = date
    return result