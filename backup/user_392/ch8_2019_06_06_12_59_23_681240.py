
def verifica_progressao(x):
    for i in range(len(x)):
        if x[i+1] == (x[i+2] + x[i])/2:
            return ('PA')
        elif x[i+1]**2 == x[i]*x[i+2]:
            return ('PG')
        elif x[i+1]**2 == x[i]*x[i+2] and x[i+1] == (x[i+2] + x[i])/2:
            return  ('AG')
        else:
            return ('NA')
        