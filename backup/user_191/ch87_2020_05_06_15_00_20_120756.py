with open('churras.txt','r') as arquivo:
    conteudo=arquivo.readlines()
    for linha in conteudo:
        linha.strip()
        x=linha.split(',')
    i=0
    soma=0
    while i<(len(x)):
        soma+=x[i][1]*x[i][2]
        i+=1
    print(soma)
        