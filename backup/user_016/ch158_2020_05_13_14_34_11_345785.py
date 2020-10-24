with open('texto.txt','r') as arquivo:
    conteudo_completo = arquivo.read()
    quantidade = conteudo_completo.splt()
print(quantidade)