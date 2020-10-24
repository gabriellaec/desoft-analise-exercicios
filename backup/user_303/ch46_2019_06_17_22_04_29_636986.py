lista_palavras1=[]
lista_palavras2=[]
a=input("Digite uma palavra:")

while a != "fim": 
    lista_palavras1.append(a)
    a=input("Digite uma palavra:")
    
for palavra in lista_palavras1: 
    if palavra[0]=="a":
        lista_palavras2.append(palavra)
print(lista_palavras2)