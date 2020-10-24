def eh_primo(x):
    y=2

    if x==2:
        return('É primo')
    
    if x==0 or x==1:
        return ('Não é primo')
    while x>y:        
        if x%y==0:
            return ('Não é primo')
            y=y+1
        else:
            return ('É primo')