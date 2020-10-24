lista=[]
a=input("Escreva palavras:")
while a!="fim":
    lista.append(a)
    a=input("Escreva palavras:")
i=0
while i<len(lista):
    palavra=lista[i]
    if len(palavra)>1 and palavra[0]=="a":
        print(palavra)
    i+=1
    


