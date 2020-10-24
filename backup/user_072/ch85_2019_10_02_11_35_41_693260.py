file = open('macacos-me-mordam.txt','r') 
conteudo = file.read()
file.close
lista = conteudo.read()
print(len(lista))