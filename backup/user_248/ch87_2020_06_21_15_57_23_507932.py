with open('churras.txt','r') as arquivo:
    conteudo=arquivo.readlines()
    total=0

    for i in conteudo:
        item=i.split(',')
        total+=int(item[1])*float(item[2])
print(total)