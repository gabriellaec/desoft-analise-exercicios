palavra = input("Digite uma palavra: ")
listaPalavras = []
listaPalavras.append(palavra)
while(palavra!="fim"):
    palavra = input("Digite uma palavra: ")
    listaPalavras.append(palavra)
i = 0
listaA = []
while(i<len(listaPalavras)):
    if(listaPalavras[i][0]== "a" or listaPalavras[i][0]== "A" ):
        listaA.append(listaPalavras[i])
    i = i + 1

print(listaA)