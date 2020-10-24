with open('dados.csv', 'r') as arquivo:
        lista = []
        lista2 = []
        conteudo = arquivo.readlines()
        for i in conteudo:
                lista.append(i.split(','))
        for i in lista:
                lista2.append(('\t').join(i))
        print(lista2)
           
with open('dados.tsv', 'w') as arquivo2:
        arquivo2.writelines(lista2)
