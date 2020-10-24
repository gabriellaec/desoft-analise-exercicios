with open('texto.txt', 'r') as arquivo:
    lista_arquivo = arquivo.read()
    
print(len(lista_arquivo.split()))
