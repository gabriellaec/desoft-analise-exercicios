with open("macacos-me-mordam.txt") as x:
    a = x.readlines()
    qtd=0
    for i in a:
        #print(i.lower().strip()=='banana')
        #print(i.lower())
        if i.lower().strip() == 'banana':
        	qtd+=1
    x.close()
print(qtd)
        
        