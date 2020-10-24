with open('churras.txt','r') as arquivo:
    curras = arquivo.readlines()
    total = 0
	for k in churras:
    	total += k['quant'] * k['preco']
    print("total: {0}".format(total))