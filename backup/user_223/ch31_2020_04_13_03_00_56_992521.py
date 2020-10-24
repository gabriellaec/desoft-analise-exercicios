def eh_primo(n):
    if n==0 or n==1 or (n%2==0 and n!=2):
        return (False)
    elif n==2:
        return (True)
    elif n%2!=0:
        impares = []
        for i in range (2, n, 2):
            while i > 0:
                impares_antes = n-i
                impares.append(impares_antes)
            for x in range (len(impares)-1):
                if n%impares[x]==0:
                    return (False)
                else:
                    return (True)