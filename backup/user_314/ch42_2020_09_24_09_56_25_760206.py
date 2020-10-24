
lista_a=[]

palavra=""

while(palavra!="fim"):
  
  palavra= input("Escreva palavras: ")
  
  if(palavra[0]=="a"):
    lista_a.append(palavra)

print(lista_a)