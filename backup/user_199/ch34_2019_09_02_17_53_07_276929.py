c=int(input("digite o deposito inicial:"))
j=int(input('digite a taxa de juros:'))

lista_montante=[]
t=0
while t<24:
    t+=1
    m=c+(c*(j/100)*t)
    lista_montante.append(m)
    
    print('{0:.2f}'.format(m))
   
i=0
while i<len(lista_montante): 
    i+=1                
    y=lista_montante[23]-lista_montante[0]
    print ('ganho com o juros: ',y)
    break
        
        
        
        
    