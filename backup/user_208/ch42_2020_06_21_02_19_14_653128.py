         
lista = []
lista1 = []
while True:
    x = str(input("Digite uma palavra: "))
    if x[0] == "a":
        lista.append(x)
    if x[0] != "a":
        lista1.append(x)
    if x == 'fim':
        i = 0
        while i < len(lista):
            print(lista[i])
            i+=1
           
    
   
        
        
        
    
    