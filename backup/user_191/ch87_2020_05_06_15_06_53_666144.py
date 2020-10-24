soma=0
with open('churras.txt','r') as arquivo:
    conteudo=arquivo.readlines()
    for linha in conteudo:
        x=linha.split(',')
        soma+=float(x[1])*float(x[2])
print(soma)        