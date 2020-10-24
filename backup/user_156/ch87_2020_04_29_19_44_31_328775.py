with open ("churras.txt", "r") as arquivo:
    conteudo = arquivo.read()
    conteudo_separado = []
    for str in conteudo: 
        for char in str: 
            try:
                num = int(char)
                conteudo_separado.append(num)
            except ValueError as verr:
                pass
    i = 1
    
    while i < len(conteudo_separado):
        conta = conteudo_separado[i] * conteudo_separado[i+1]
        
        i+=2
        
    print(conta)
        
    
    
    