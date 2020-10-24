x=True
ls=[]
while x:
    num=int(input("Digite um número positivo e inteiro: "))
    if num<=0:
        x=False
    else:
        ls.append(num)
lengh=len(ls)-1
i=0
lista=[]
while i<=len(ls)-1:
    lista.append(ls[lengh])
    i+=1
    lengh-=1
print(lista)  
    