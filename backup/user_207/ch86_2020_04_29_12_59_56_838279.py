with open ('arquivo.csv', 'r') as arquivo:
    leitura = arquivo_csv.read() #lê o arquivo e o transforma em uma String
    leitura = leitura.replace (',', '\t') #substitui as vírgulas por \t e, assim, transforma CSV em TSV
    arquivo.write(leitura)
	