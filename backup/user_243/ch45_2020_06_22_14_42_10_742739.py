a=input("digite numeros inteiros positivos")
lista=[]
i=0
while i<len(a):
    lista.append(a)
    if a<0 or a==0:
        print(lista[::-1])
        
