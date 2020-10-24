'''def conta_palavras(teste):
    with open(teste, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()         
        i = 0
        for p in palavras:
            if p.lower() == 'banana':
                i += 1            
            if p.lower() == 'banana.':
                i += 1
    return i        
print(conta_palavras('macacos-me-mordam.txt'))'''

def conta_bananas(arquivo):
    contador = 0
    
    #abre o arquivo para o modo leitura (r)
    with open(arquivo, 'r') as arquivo_texto:
        #faz a leitura do arquivo
        conteudo = arquivo_texto.read()
        #faz uma lista com cada palavra separada.
        lista_palavras = conteudo.split()

        for palavra in lista_palavras:
            if palavra.lower() == 'banana':
                contador += 1
    
    return contador


print(conta_bananas('macacos-me-mordam.txt'))