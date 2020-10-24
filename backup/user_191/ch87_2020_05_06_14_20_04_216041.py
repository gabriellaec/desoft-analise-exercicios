with open('churras.txt','r') as arquivo:
    conteudo=arquivo.read()
    conteudo.split(',')
    conteudo.split('\n')
    i=0
    soma=0
    while i<(len(conteudo)-2):
        i+=1
        soma=conteudo[i]*conteudo[i+1]
        i+=2
    print(soma)
        