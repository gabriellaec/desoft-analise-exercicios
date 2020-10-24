

lista=[]
lista_a=[]

palavra=""

while(palavra!="fim"):
  
    palavra= input("Escreva palavras: ")
    lista.append(palavra)

    if(palavra[0]=="a"):
        lista_a.append(palavra)

for i in lista_a:
    print(i)