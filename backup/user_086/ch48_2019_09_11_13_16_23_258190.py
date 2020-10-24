strmes=input('qual o nome do mês escolhido? ')
contador=0
while contador<len(listastr):
    if strmes==listastr[contador]:
        print(contador+1)
    contador+=1