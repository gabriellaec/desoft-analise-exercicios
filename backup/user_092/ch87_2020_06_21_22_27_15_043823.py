with open('churras.txt','r') as arquivo:
    cc = arquivo.read()
    c = 0
    while c<len(cc):
        if cc[i] == \ and cc[i+1] == n:
            del cc[i]
            del cc[i+1]
        i += 1
            
    r = c1.strip()
    L = r.split(',')
    i = 2
    valor = 0
    while i <= len(L):
        n = float(L[i])
        valor += n
        i += 3
    print(valor)