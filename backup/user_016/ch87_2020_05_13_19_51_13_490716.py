with open('churras.txt','r') as arquivo:
    conteudo = arquivo.readlines()
    for i in conteudo:
        separa = conteudo.split(',')
        preço.append(separa[1]*separa[2])
print(sum(preço))
    