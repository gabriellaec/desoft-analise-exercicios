def eh_bissexto(ano):
    resto1=ano%4
    resto2=ano%100
    if resto1==0 and resto2!=0:
        return True
    else:
        return False
        
    
        