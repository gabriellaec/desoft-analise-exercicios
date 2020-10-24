def eh_primo(n):
    Troca = True
    final = True
    div = 2
    if( n == 0 and n == 1):
        final = False
    while(div <= n/2 and Troca):
        resp = n % div
        if resp == 0 :
            final = False
            Troca = False
        else:
            div +=1
    return final
            
        