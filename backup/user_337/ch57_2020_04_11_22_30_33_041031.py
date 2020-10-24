def verifica_progressao(lista):
    i = 0 
    pa1 = []
    pa2 = []
    pg1 = []
    pg2 = []
    while i < 0:
        pa1 = lista[i+1] - lista[i]
        pa2 = lista[i+2] - lista[i+1]
        pg1 = lista[i+1] / lista[1]
        pg2 = lista[i+2] / lista[i+1]
        if pa1 == pa2 and pg1 == pg2:
            
            