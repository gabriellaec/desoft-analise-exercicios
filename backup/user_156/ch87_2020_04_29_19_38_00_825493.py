with open ("churras.txt", "r") as arquivo:
    conteudo = arquivo.read()
    
    conteudo_separado = conteudo(map(int(conteudo.split())))
    i = 1
    
    while i < len(conteudo_separado):
        conta = conteudo_separado[i] * conteudo_separado[i+1]
        
        i+=2
        
    print(conta)
        
        
    
    