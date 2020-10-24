soma=0
with open('churras.txt','r') as arquivo:
    a=arquivo.readlines()
    for i in b:
        linha=i.split()
        soma+=float(linha[1])*float(linha[2])
print(soma)