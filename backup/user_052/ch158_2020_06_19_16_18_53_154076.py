with open ("texto.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    i = 0
    soma = 0
    while i < len(x):
        soma += 1
        i += 1
    print (soma)
    
    
    #print (len(x))