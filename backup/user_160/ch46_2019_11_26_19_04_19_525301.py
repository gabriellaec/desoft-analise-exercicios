lista = []
i = 0
palavra = input("Qual a palavra desejada?")
lista.append(palavra)
while palavra != "fim":
    palavra = input("Qual a palavra desejada?")
    lista.append(palavra)
while i <= len (lista):
    if lista [i][0] == 'a':
        print (lista[i])
    i += 1
        


    
   