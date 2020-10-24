#a ou A
arquivo=open('palavras.txt','r')
conteudo=arquivo.read()
arquivo.close()

conteudo=conteudo.split(' ')
print(conteudo)
#conteudo é uma lista de palavras agora
i=0
comecam=0
while i<len(conteudo):
    if conteudo[i][0]=='a' or conteudo[i][0]=='A':
        comecam+=1
    i+=1
print(comecam)