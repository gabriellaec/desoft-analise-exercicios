with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    
import re
lista = re.split('\n |, ', conteudo)
qtd = 0
preço = 0
for i in range(len(lista) - 2):
    qtd = lista[i+1]
    preço = qtd*lista[i+2]
    
print(preço)