divisores = []
def eh_primo(x):
    for i in range(1,x+1):
        if x%i == 0:
            divisores.append(i)
    if len(divisores)>2 or x== 1 or x==0:
        print("nao eh primo")
    else:
        print("eh primo")
        
        
  


 
     
    
