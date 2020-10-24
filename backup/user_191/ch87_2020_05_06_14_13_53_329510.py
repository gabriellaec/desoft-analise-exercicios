with open('churras.txt','r') as arquivo:
    conteudo=arquivo.read()
    conteudo.split('\n')
    conteudo.split(',')
    i=0
    soma=0
    while i<(len(conteudo-3)):
        i+=1
        soma=i*(i+1)
        i+=2
    print(soma)
        