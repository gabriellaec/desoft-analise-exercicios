with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo=conteudo.lower()
    arroz=conteudo.split()
    a=0
    i=0
    cont=0
    lista_vazia=[]
for d in arroz:
    if d =='banana':
        i+=1
print(i)