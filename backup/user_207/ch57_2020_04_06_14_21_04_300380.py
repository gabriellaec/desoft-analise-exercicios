lista =[]

def verifica_progressao (lista):
    i=0
    while i<len(lista):
        lista_razao =[]
        razao = lista[i+1] - lista[i]
        lista_razao.append (razao)
    
        lista_quociente =[]
        quociente = lista[i+1]/lista[i]
        lista_quociente.append (quociente)
        
        for r,q in lista_razao, lista_quociente:
            if e == razao:
                print ('PA')
            if q == quociente:
                print ('PG')
            if e == q:
                print ('AG')