lista=[]
i=0
p=1
while(p!='fim'):
    p=input("escreva uma palavra(quando quiser parar, escreva'fim'")
    lista.append(p)
for i in range(0,len(lista)):
    if lista[i][1]=='a':
        print(lista[i])