with open('churras.txt','r') as arquivo:
    curras = arquivo.read()
    total = 0
	for k in churras['itens']:
    	total += k['quant'] * k['preco']
    print("total: {0}".format(total))