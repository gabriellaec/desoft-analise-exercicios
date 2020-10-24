valor=0.00
with open ('churras.txt','r') as arquivo:
    a=arquivo.readlines()
    for linha in linhas: 
        l=linha.split(',')
        valor+=float(l[1])*float(l[2])
 
print(valor)