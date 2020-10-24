def conta_palavras(texto):
    with open (texto, 'r') as arquivo:
        conteudo=arquivo.read()
        palavra=split.split()
        return len(palavra)
print(conta_palavras('texto.txt'))
        
    

    