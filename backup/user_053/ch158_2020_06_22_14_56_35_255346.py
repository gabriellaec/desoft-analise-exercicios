with open('texto.txt', 'r') as arquivo:
    # Transforma numa string
    conteudo = arquivo.read()
    # Remove espaços em branco
    conteudo = conteudo.strip()
    # Retorna lista separando palavras
    conteudo = conteudo.split()
    
print(len(conteudo))