lista=[]
i=True 
while i:
    n = int(input("digite numeros"))
    lista.append(n)
    if n<=0:
        n = lista[::-1]
        print(n)
        
    