#São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
#São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
#Não são bissextos todos os demais anos.
def eh_bissexto(x):
    if x%4 == 0:
        if x%400 == 0:
            return True
        elif x%100 == 0:
            return False
        else:
            return True
     
 
    else:
        return False
        
 
 
 
        
 