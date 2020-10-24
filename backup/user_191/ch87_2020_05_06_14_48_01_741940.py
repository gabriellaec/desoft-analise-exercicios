with open('churras.txt','r') as arquivo:
    conteudo=arquivo.read()
    x=conteudo.split(',')
    y=' '.join(x)
    z=y.split('/n')
    i=0
    soma=0
    while i<(len(z)-3):
        i+=1
        soma=z[i]*z[i+1]
        i+=2
    print(soma)
        