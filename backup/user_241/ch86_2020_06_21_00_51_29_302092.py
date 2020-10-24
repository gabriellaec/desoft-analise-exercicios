arquivo = open('dados.csv','r')
lista = arquivo.readlines()
arquivo.close()
for linha in lista:
    linha = linha.replace(',','\t')
arquivo2 = open('dados.tsv','w')
arquivo2.writelines(lista)
arquivo2.close()