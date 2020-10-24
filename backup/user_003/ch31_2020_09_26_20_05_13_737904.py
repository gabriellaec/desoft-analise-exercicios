def eh_primo(n):
    Troca = True
    final = False
    div = 2
    if( n == 0 and n == 1):
        final = True
    while(div <= n/2 and Troca):
        resp = n % div
        if resp == 0 :
            final = True
            Troca = False
        else:
            div +=1
    return final
            
        