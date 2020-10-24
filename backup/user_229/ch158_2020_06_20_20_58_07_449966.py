with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    
lista = texto.split()
print(len(lista))