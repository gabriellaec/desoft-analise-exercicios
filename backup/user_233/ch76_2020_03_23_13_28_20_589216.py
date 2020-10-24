def aniversariantes_de_setembro(aniversarios):
    
    setembro = dict()
    
    for pessoa in dic.keys():
        data = aniversarios[pessoa].split('/')
        if int(data[1]) == 9: setembro[pessoa] = aniversarios[pessoa]
    
    return setembro