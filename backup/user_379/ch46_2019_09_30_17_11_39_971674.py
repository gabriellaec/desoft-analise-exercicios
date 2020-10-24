lista=[]
i=0
palavra=True
while palavra:
    a=input("digite uma palavra ")
    if a[0]=="a":
        lista.append(a)
    elif a=="fim":
        print(lista[i])
        palavra=False
    i+=1
