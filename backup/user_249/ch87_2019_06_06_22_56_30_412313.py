soma=0
with open('churras.txt','r') as arquivo:
    a=arquivo.readlines(',')
    for i in a:
        l=i.split()
        soma+=float(l[1])*float(l[2])
print(soma)