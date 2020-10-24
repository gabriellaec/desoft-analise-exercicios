with open('macacos-me-mordam.txt', 'r') as arquivo:
    leitura = arquivo.read() #lê o arquivo e armazena em uma única string
    leitura = leitura.lower() #reduz todos os caracteres p/ minúsculas


lista_de_palavras = leitura.split()
count = 0
for elemento in lista_de_palavras:
    if elemento == 'banana':
        count +=1
        
print (count)