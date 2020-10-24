lista_palavras = ['']

while(True):
    palavra = input("Escolha uma palavra: ")
    lista_palavras.append(palavra)
    if palavra == "fim":
        break
        
for palavras in range(len(lista_palavras)):
    palavra = lista_palavras[palavras]
    if palavra[0] == 'a':
        print(palavra)