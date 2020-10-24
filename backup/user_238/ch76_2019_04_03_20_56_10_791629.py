def aniversariantes_de_setembro(info):  
    dicionario={}
    for n,m in info.items():
            if m[3:5]=='09':
               	dicionario[n]=m
    return dicionario
niver={'ana':'03/04/2000', 'julia': '03/07/1234'}
print(aniversariantes_de_setembro(niver))
