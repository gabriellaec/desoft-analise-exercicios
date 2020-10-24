soma=0
with open('churras.txt','r') as arquivo:
    a=arquivo.readlines()
    for i in a:
        i=i.split()
        soma+=float(i[1])*float(i[2])
print(soma)