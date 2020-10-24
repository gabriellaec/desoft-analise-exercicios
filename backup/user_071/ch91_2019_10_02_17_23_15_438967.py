with open('palavras.txt', 'r') as arquivo:
    contagem=0
    for i in arquivo:
        if i[0]=='a' or i[0]=='A':
            contagem+=1
    print(contagem)