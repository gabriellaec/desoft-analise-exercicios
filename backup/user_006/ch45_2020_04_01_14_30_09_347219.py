ok=True
lista=[]
while ok:
    num=int(input("Digite um numero inteiro positivo"))
    if num>0:
        lista.append(num)
    else:
        i=len(lista)
        while i>0:
            print(lista[i-1])
            i=i-1
        
