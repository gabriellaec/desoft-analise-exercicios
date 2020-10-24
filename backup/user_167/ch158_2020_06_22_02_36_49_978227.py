with open ('texto.txt','r') as arquivo:
    cont=arquivo.readlines()
    i=0
    for e in cont:
        i+=1
    print(i)