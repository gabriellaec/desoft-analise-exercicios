def verifica_progressao(x):
    x = []
    i = 0
    while i < len(x):
        if x[i+1] == (x[i+2] + x[i])/2:
            print ('PA')
        elif x[i+1]**2 == x[i]*x[i+2]:
            print ('PG')
        elif x[i+1]**2 == x[i]*x[i+2] or x[i+1] == (x[i+2] + x[i])/2:
            print  ('AG')
        else:
            print ('NA')
        i += 1
