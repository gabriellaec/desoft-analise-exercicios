with open('macacos-me-mordam.txt', 'r') as arquivo:
    # Transforma arquivo numa única string
    sentenca = arquivo.read()
    # Remove caracteres em branco e \n
    sentenca_limpa = sentenca.strip()
    # Faz listagem das palavras
    lista = sentenca_limpa.split()

contador = 0
for i in lista:
    if i == 'banana' or i == 'Banana' or i == 'BANANA' or i = 'BaNaNa':
        contador += 1

print(contador)