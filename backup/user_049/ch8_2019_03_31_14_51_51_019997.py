def verifica_progressao(n):
    i=0
    pa=[i]-n[i+1]
    pg=[i]/n[i+1]
    while i<len(n):
        if pa==[i+1]-n[i+2] and pg==[i+1]/n[i+2]:
            print('AG')
        elif pa===[i+1]-n[i+2]:
            print('PA')
        elif pg==[i+1]/n[i+2]:
            print('PG')
        else:
            print('NA')
        i+=1