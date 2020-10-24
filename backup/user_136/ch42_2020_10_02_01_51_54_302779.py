lista= []
controle= True
while controle:
    palavra= input('qual a palavra? ')
    primeira_letra= palavra[0]
    if primeira_letra=='a':
        lista.append (palavra)
    elif palavra=='fim':
        controle= False
print (lista)