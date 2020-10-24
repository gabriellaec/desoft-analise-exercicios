with open ("texto.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    soma = 0
    for i in range(len(x)-1):
        soma += 1
    print (soma)
    
    
    #print (len(x))