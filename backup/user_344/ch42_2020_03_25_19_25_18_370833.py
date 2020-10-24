palavra = input("Escreva uma palavra")
lista = []
while palavra != 'fim':
    palavra = input("Escreva uma palavra")
    lista.append(palavra)
i=0
while i<len(lista):
    if palavra[0] == 'a' or palavra[0] == 'A':
        palavraA = palavra
        print (palavraA)
    i+=1
        
    
