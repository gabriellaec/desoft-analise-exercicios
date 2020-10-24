arq1 = open('palavras.txt','r')
conteudo = arq1.read()
arq1.close()

conteudo = conteudo.split()
cont = 0
for i in conteudo:
    if i[0] == 'a' or i[0] == 'A':
        cont += 1
        
print(cont)