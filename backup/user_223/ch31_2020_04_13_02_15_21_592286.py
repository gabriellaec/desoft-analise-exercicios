def eh_primo(n):
    if n%2==0:
        impares=[]
        for i in range (1, n, 2):
            impares_antes = n-i
            impares.append(impares_antes)
            for x in range (len(impares)):
                if n%impares_antes[x]==0:
                    return (False)
                else:
                    return (True)
    elif n%2!=0:
        impares2 = []
        for i in range (n):
            impares_antes2 = n-1
            impares2.append(impares_antes2)
            for y in range (len(impares2)):
                if n%impares_antes[y]==0:
                    return (False)
                else:
                    return (True)