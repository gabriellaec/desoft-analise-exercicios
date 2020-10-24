with open ('dados.csv', 'w') as arquivo_csv:
    leitura = arquivo_csv.read() #lê o arquivo e o transforma em uma String
    leitura = leitura.replace (',', "\t") #substitui as vírgulas por "\t" e, assim, transforma CSV em TSV
    leitura.write()

	