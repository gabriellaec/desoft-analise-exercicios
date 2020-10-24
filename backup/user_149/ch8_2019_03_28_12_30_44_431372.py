def verifica_progressao(lista):
    i=0
    while i<len(lista):
        razaoPA = lista[1]-lista[0]
        razaoPG = lista[1]/lista[0]
        i+=1
    if lista[2]==lista[1]+razaoPA and lista[2]!=lista[1]+razaoPG:
        print('PA')
    elif lista[2]==lista[1]+razaoPG and lista[2]!=lista[1]+razaoPA:
        print('PG')
    elif lista[2]==lista[1]+razaoPA and lista[2]==lista[1]+razaoPG:
        print('AG')
    elif lista[2]!=lista[1]+razaoPA and lista[2]!=lista[1]+razaoPG:
        print('NA')