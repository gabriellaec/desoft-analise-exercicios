def aniversariantes_de_setembro (dic):
    
    setembro={}
    
    for i in dic.keys():
        if(dic[i][4]== '9'):
            setembro[i]=dic[i]

    return setembro