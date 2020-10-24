with open("palavras.txt","a") as arquivo:
    conteudo = arquivo.write()
    contador = 0
    for i in conteudo:
        if i[0]=='a' or i[0]=='A':
            contador+=1
            

print(contador)