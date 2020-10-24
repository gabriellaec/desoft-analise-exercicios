listapalavras=[]
palavra=input('Digite alguma palavra: ')
while palavra!='fim':
    listapalavras.append(palavra)
    palavra=input('Digite alguma palavra: ')
i=0
while i<len(listapalavras):
    palavra=listapalavras[i]
#as strings funcionam como listas também, então se chamarmos um termo de outro termo da lista mais externa, podemos acessar as letras da string
    if palavra[0]=='a' or palavra[0]=='A':
        print(palavra)
    i+=1