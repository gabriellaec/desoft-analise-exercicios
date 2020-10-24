with open('churras.txt', 'r', encoding="utf8") as arquivo:
        lista = []
        valor  =  0
        quantidade = []
        preço = []
        conteudo = arquivo.readlines()
        for i in conteudo:
                lista.append(i.split(','))

        for i in lista:
                quantidade.append(i[1])
                preço.append(i[2])
        
        for i in range(0,len(quantidade)):
                valor += float(quantidade[i]) * float(preço[i])
        print(valor)
