with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.lower()
    
    i=0
    cont=0
    lista_vazia=[]
    while i<len(conteudo):
        lista_vazia.append
        if conteudo[i] == ' ':
            lista_vazia.append(conteudo[:i])
            if 'banana' in lista_vazia[-1]:
                cont+=1
	print(cont)
        