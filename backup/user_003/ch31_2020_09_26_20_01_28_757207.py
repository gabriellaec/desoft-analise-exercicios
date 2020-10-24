def eh_primo(n):
    final = True
    div = 2
    while(div <= n/2 and final):
        resp = n % div
        if resp == 0 :
            final = False
        else:
            div +=1
    return final
            
        