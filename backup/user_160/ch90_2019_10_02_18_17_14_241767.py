def segundos_entre(hd1,hd2):
    lista = ['hd1']
    lista2 = ['hd2']
    
    calculo1 = lista2[0][0] - lista[0][0]
    calculo2 = lista2[0][1] - lista[0][1]
    calculo3 = lista2[0][2] - lista[0][2]
    calculototal = calculo3 + calculo2*60 + calculo1*3600
    print(calculototal)