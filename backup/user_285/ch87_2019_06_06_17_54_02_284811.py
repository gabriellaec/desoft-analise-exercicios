with open("churras.txt",'r') as arquivo:
    churrasco=arquivo.read()
churrascolista=churrasco.split(',')
contador=0
contador1=1
contador2=2
soma=0
while contador<len(churrascolista):
    produto=churrascolista[contador1]*churrascolista[contador2]
    total+=produto
    contador+=0
    contador1+=2
    contador2+=2
print(total)