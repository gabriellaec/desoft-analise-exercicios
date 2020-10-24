soma=0
with open('churras.txt','r') as arquivo:
    conteudo=arquivo.readlines()
    for linha in conteudo:
        x=linha.split(',')
        soma+=float(linha[1])*float(linha[2])
        i+=1
print(soma)        