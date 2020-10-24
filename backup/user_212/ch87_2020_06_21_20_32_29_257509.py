lista =[]

with open ('churras.txt', 'r') as arquivo:
    conteudo_linhas = arquivo.readlines()
    
    for linha in linhas:
        lista.append(i.split(','))  #vai adicionar na lista uma lista 
                                    #menos que foi criada ao separar o texto nas virgulas
total = 0
for i in lista: #para cala elemento na lista menor dentro da lista
    total += int(i[1]) * float(i[2])
    
print(total)