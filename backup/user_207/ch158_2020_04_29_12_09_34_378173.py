with open ('texto.txt', 'r') as arquivo:
    leitura = arquivo.read()
def contador_de_palavras(leitura):
    lista_de_palavras = leitura.split() #qnd não tem argumento, ele usa o ESPAÇO como separador
    count = len(lista_de_palavras)
    return count