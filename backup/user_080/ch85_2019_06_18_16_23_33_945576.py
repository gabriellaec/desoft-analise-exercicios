with open("macacos-me-mordam.txt") as x:
    a = x.read()
    qtd=0
    for i in a:
        if i.lower() == 'banana':
        	qtd+=1
    x.close()
print(qtd)
        
        
        