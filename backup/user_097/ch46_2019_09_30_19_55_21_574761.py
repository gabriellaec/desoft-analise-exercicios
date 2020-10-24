palavra = input("Digite uma palavra: ")
listaPalavras = []
listaPalavras.append(palavra)
while(palavra!="fim"):
    palavra = input("Digite uma palavra: ")
    listaPalavras.append(palavra)
i = 0
listaA = []
while(i<len(listaPalavras)):
    if(listaPalavras[i][0]== "a"):
        print(listaPalavras[i])
    i = i + 1