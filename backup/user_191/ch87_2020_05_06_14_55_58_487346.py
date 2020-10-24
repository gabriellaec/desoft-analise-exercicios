with open('churras.txt','r') as arquivo:
    conteudo=arquivo.readlines()
    for linha in conteudo:
        linha.strip()
        x=linha.split(',')
    i=0
    soma=0
    while i<(len(x)-3):
        i+=1
        soma=x[i]*x[i+1]
        i+=2
    print(soma)
        