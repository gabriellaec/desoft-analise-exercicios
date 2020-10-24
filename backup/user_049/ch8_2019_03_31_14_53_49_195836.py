def verifica_progressao(n):
    i=0
    pa=[i]-n[i+1]
    pg=[i]/n[i+1]
    while i+2<len(n):
        if pa==n[i+1]-n[i+2] and pg==n[i+1]/n[i+2]:
            print('AG')
        elif pa==n[i+1]-n[i+2]:
            print('PA')
        elif pg==n[i+1]/n[i+2]:
            print('PG')
        else:
            print('NA')
        i+=1