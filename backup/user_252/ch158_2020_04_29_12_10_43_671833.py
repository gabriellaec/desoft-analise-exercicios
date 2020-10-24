def palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo=arquivo.read()
        palavra=conteudo.split()
        return len(palavra)
        
    

    