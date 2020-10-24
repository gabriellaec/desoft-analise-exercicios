with open ('texto.txt', 'r') as arquivo:
    leitura = arquivo.read()

lista_de_palavras = leitura.split() #qnd não tem argumento, ele usa o ESPAÇO como separador
count = len(lista_de_palavras)