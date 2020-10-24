with open('churras.txt','r') as arquivo:
    curras = arquivo.readlines()
    total = 0
	for k in churras:
        k=k.split(',')
    	total += k[1] * k[2]
    print("total: {0}".format(total))