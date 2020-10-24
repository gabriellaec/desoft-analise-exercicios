with open ('palavras.txt','r') as arquivo:
    palavras =[]

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    x=0
    for i in range(len(palavras)):
        if palavras[i][0]=='a' or palavras[i][0]=='A':
            x+=1

print(x)        