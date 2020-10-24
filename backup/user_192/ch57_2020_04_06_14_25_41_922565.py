def verifica_progressao(n):
    for i in range (len(n)):
        r1 = n[i+1] - n[i]
        r2 = n[i+1]/n[i]
        if n[i+1] == n[i] + r1:
            return 'PA'
        elif n[i+1] == n[i]*r2:
            return 'PG'
        elif n[i+1] == n[i] + r1 and n[i+1] == n[i]*r2:
            return 'AG'
        else:
            return 'NA'
        