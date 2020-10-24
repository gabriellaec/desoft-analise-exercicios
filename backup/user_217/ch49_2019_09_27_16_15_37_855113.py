lista=[]
verifica=True 

while verifica:
    
    n = int(input("Digite o numero: "))
    
    if n == 0 or n/1<0:
        lista.reverse()
        print(lista)
        break
        
    else: 
        lista.append(n)
        