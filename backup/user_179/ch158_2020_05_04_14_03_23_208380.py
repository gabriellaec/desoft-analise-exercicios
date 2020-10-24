with open('texto.txt','r') as texto:
    conteudo = texto.read()
    
palavras = conteudo.split()
contador = len(palavras)

print(contador)