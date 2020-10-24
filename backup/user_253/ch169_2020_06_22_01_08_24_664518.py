nome=0
lista=[]
i=1
while nome !='fim':
    nome=input('a')
    lista.append(nome)
    if nome not in lista:
        print (nome)
    else:
        for name in range(len(lista)):
            while nome in lista: 
                nome = nome +str(i)
                if nome in lista:
                    nome= nome[:-1]
                i+=1
            print (nome)
    