def primos_entre(a, b):
    if( a>1 and b>a):     
        for  primeirocontador in range(a,b+1):        
            primo=True        
            for divisordosegundofor in range(2,primeirocontador):            
                if(primeirocontador%divisordosegundofor==0):                
                    primo=False                
                    break        
                if primo:            
                    cont=cont+1print(cont)
                    


