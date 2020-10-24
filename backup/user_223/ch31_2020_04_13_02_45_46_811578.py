def eh_primo(n):
    if n==0 or n==1 or (n%2==0 and n!=2):
        return (False)
    elif n==2:
        return (True)
    elif n%2!=0:
        impares = []
        for i in range (n):
            impares_antes = n-1
            impares.append(impares_antes)
            for x in range (len(impares)-1):
                if n%impares[x]==0:
                    return (False)
                else:
                    return (True)