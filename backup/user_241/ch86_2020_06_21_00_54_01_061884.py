arquivo = open('dados.csv','r')
lista2 = []
lista = arquivo.readlines()
arquivo.close()
for linha in lista:
    a = linha.replace(',','\t')
    lista2.append(a)
arquivo2 = open('dados.tsv','w')
arquivo2.writelines(lista2)
arquivo2.close()