with open ('texto.txt','r') as arquivo:
    leitura = arquivo.read
    palavras = leitura.split()
print (len(palavras))