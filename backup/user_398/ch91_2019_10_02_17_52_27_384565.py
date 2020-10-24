with open("palavras.txt","r") as arquivo:
    a=arquivo.read()
    
minusculo=a.lower()
separado=minusculo.split()

contador=0
for e in separado:
    if e[0]=="a":
        contador+=1
    
print('existem {0} palavras que comecam com a letra a'.format(contador))