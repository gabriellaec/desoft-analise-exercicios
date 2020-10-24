lista= []
palavra= 10
while palavra!= 'fim':
    palavra= input('qual a palavra? ')
    primeira_letra= palavra[0]
    if primeira_letra =='a':
        lista.append (palavra)
print (lista)