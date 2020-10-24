with open('arquivo.txt','r') as arquivo:
    c = arquivo.read()
    conteudo = c.lower()
    lista = conteudo.split()
    l = []
    for p in lista:
        if p[0] == 'a':
            l.append('a')
            
print(len(l))