with open ('churras.txt','r') as arquivo:
    linhas=arquivo.readlines()

preco=0

for linha in linhas:
    palavras=linha.split(',')
    qnt=int (palavras [1])
    x=palavras[2].strip ('\n')
    p=float(x)
    z=qnt*p
    preco+=z