with open('churras.txt','r') as arquivo:
    conteudo=arquivo.read()
    x=conteudo.split(',')
    y=' '.join(x)
    z=y.split('/n')
    a=' '.join(z)
    b=a.split(',')
    i=0
    soma=0
    while i<(len(b)-3):
        i+=1
        soma=b[i]*b[i+1]
        i+=2
    print(soma)
        