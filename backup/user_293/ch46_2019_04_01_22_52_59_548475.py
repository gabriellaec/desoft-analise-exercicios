p= input("digite uma palavra('fim' termina): ")
lista= []
while p!= "fim":
    lista.append(p)
    p= input("digite uma palavra('fim' termina): ")
contador= 0
while contador<len(lista):
    if lista[contador][0]== "a":
        print(lista[contador])
    contador+= 1
    
   