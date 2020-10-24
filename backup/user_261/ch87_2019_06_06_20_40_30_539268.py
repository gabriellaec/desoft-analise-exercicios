valor=0.00
with open ('churras.txt','r') as arquivo:
    a=arquivo.read()
    b=a.split()
    for palavra in b:
        if palavra==float:
            valor+=palavra
     
print(valor)
    