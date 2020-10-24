with open('texto.txt', 'r') as arquivo:
    leitura = arquivo.read()

separador = leitura.split()
print(len(separador))