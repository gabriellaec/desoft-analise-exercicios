def aniversariantes_de_setembro(dict1):
    dict2=dict()
    for k,v in dict1.items():
        if dict1[k][3:5]=='09':
            dict2[k]=v
    return dict2 
            
        