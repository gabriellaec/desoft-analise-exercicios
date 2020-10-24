n= input("Digite uma palavra (termina com 'fim'): ")
lista = []
while n != "fim":
    lista.append(n)
    n= input("Digite uma palavra (termina com 'fim'): ")
i = 0
while i < len(lista):
    if lista[i][0] == "a":
        print(lista(i))
    i+=1
    
   