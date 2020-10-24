with open ('dados.csv', 'r') as arquivo_csv:
    leitura = arquivo_csv.read() #lê o arquivo e o transforma em uma String

leitura = leitura.replace (',', '	') #substitui as vírgulas por 	 e, assim, transforma CSV em TSV

#obs.: eu poderia fazer em 2 etapas
# 1- string.split(','): pega a string, separa os dados pelas ',' e cria uma lista
# 2- '	'.join (lista): pega os elementos da lista e intercala eles com 	