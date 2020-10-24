with open ('churras.txt','r') as arquivo:
    conteudo=arquivo.read()
conteudo=conteudo.replace('\n',',')
conteudo=conteudo.split(',')
i=0
total=0
while i < len(conteudo):
    soma=int(conteudo[i+1])*float(conteudo[i+2])
    total+=soma
    i+=3
print(total)