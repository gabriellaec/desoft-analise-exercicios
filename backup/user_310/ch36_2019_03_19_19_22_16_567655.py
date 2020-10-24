def eh_primo(n):
    i=2
    validacao= 0
    
    while i<n:
        if n%i==0:
            validacao=1
            return "não é primo"
        i+=1
    
    if validacao==0:
        return "primo"
        