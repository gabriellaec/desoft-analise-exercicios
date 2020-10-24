lista=[]
i=True 
while i:
    n = int(input("digite numeros"))
    if n>0:
        lista.append(n)
    else:
        lista = lista[::-1]
        print(lista)
        break
    