def verifica_quadrado_perfeito(n):
    num=len(x)
    i=0
    x=1
    quadrado_perfeito=n[i]-x
    while i<num and n[i]>0: 
        if n[i]-x==0:
            quadrado_perfeito=True
        elif n[i]-x<0:
            quadrado_perfeito=False
        else:
            x+=2
            i+=1
print(quadrado_perfeito)
            
            
        
        
       
            
    
    
    
