
def verifica_progressao(x):
    for i in range(len(x)):
        if x[i+1] == (x[i+2] + x[i])/2:
            print ('PA')
        elif x[i+1]**2 == x[i]*x[i+2]:
            print ('PG')
        elif x[i+1]**2 == x[i]*x[i+2] and x[i+1] == (x[i+2] + x[i])/2:
            print  ('AG')
        else:
            print ('NA')
        return x
        