Entrada= {'Andrew Ayres': 30, 'Fábio Ikeda': 25, 'Fábio Kurauchi': 25, 'Raul Hage': 28}
def inverte_dicionario(x):
    lista_reserva = {}
    for i in x:
        if x[i] not in lista_reserva:
            lista_reserva[x[i]] = [i]
        else:
            lista_reserva[x[i]].append(i)
        
    return lista_reserva

def capitaliza(x):
    x = str(x)
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if alfabeto.find(x[0]) != -1:
        comeco = ALFABETO[alfabeto.find(x[0])]
        final = x[1:]
    elif ALFABETO.find(x[0]) != -1:
        comeco = alfabeto[ALFABETO.find(x[0])]
        final = x[1:]
    return comeco + final