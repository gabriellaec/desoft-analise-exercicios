with open('churras.txt','r') as arquivo:
    total=0
    conteudo=arquivo.read()
    teste=conteudo.splitlines()

    for i in range(0,(len(teste))):
        produto= teste[i].split(',')
        total+=(float(produto[1])*float(produto[2]))
        print (total)
        
    