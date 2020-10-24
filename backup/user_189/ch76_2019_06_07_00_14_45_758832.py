def aniversariantes_de_setembro(dic):
    setembro=9
    saida={}
    for a in dic.values():
        if a[3]==9:
            saida[a]=a[3]
   	
    return saida
            
        