with open ('dados.csv', 'r') as arquivo:
    leitura = arquivo_csv.read() #lê o arquivo e o transforma em uma String
    leitura = leitura.replace (',', '	') #substitui as vírgulas por 	 e, assim, transforma CSV em TSV
    arquivo.write(leitura)
	