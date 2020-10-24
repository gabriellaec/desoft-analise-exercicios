valor=0.0
with open ('churras.txt','r') as arquivo:
    a=arquivo.readlines()
    for linha in a: 
        l=linha.split(',')
        valor+=float(l[1])*float(l[2])
 
print(valor)