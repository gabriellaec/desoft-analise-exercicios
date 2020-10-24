with open("churras.txt", "r")as arq:
    conteudo=arq.readlines()
    valor=0
for i in conteudo:
    item=i.split()
    valor+=float(item[1])*float(item[2])
print (valor)
        
    