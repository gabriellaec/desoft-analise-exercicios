def eh_primo(n):
    final = True
    div = 2
    while(d <= n/2 and final):
        resp = n % d
        if resp == 0 :
            final = False
        else:
            d +=1
    return final
            
        