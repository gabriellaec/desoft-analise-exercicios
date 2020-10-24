def eh_bissexto(ano):
    resto1=ano%4
    resto2=ano%100
    resto3=ano%400
    if resto3==0:
        return True
    else:
        if resto2==0:
        	return False
    else:
        if resto1==0:
        return True
    
    