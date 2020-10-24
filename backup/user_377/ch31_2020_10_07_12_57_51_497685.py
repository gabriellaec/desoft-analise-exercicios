def eh_primo(numero):
    if numero < 2:
        primo= False    
    primo = True
    while 2 < numero:
        if numero % 2 == 0:
            primo= False
        else:
            primo = True
        