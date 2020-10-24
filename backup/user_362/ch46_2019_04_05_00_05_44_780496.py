lista=[]
palavra=(input("digite uma palavra"))
contador=0
while palavra!='fim':
    lista.append(palavra)
    palavra=(input("digite uma palavra"))
    if lista[contador][0]=='a':
        print lista[contador]
    contador+=1
    