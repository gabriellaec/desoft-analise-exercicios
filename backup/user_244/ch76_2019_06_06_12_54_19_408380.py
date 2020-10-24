def aniversariantes_de_setembro(x):
    x = dict()
    z = dict()
    
    
    
    valores = x.values()
    for i in valores: 
        if i[4] == "9":
            for e in x.keys():
                z = {x[e]:x[i]}
    
    return z 




    