def verifica_progressao (lista):
    pa = True
    pg = True
    
    if len(lista) == 0:
       
        pa = False
        pg =False
    else:
        
        for i in lista:
            if i == 0:
                return("NA")
            
        aumento = lista[1] - lista[0]
        razao = lista[1]/lista[0]
        
        for i in range (len(lista)-1):
             
            if lista[i+1] - lista[i] != aumento:
                pa = False  
            elif lista[i+1] / lista[i] != razao:
                pg = False
                
        if pa == True and pg == False:
            return ("PA")
        elif pa == False and pg ==True:
            return ("PG")
        elif pa== False and pg==False:
            return("NA")
        elif pa==True and pg== True:
            return ("AG")
        
        
            
        