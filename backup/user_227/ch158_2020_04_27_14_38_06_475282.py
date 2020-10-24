arquivo=open("texto.txt", "r")
conteudo=arquivo.read()
lista_arquivo=conteudo.split()
print(len(lista_arquivo))