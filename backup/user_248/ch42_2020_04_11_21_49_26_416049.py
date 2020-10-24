lista=[]
palavra=input("Palavra:")
while palavra!="fim":
    lista.append(palavra)
    palavra=input("Outra Palavra:")
i=0
while i<len(lista):
    palavra=lista[i]
    if palavra[0]=="a":
        print(palavra)
    i+=1
              