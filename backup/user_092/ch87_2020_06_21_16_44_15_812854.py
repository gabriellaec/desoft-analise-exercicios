with open('churras.txt','r') as arquivo:
    cc = arquivo.read()
    r = cc.replace('\n',',')
    L = r.split(',')
    i = 2
    valor = 0
    while i <= len(L):
        n = float(L[i])
        valor += n
        i += 3
    print(valor)