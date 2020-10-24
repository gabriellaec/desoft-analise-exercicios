def eh_primo(ano):
    if ano%2 and not ano==2:
        return False
    elif ano%3 and not ano==3 or ano%5 and not ano==5:
        return False
    elif ano==0 or ano==1:
        return True
    else:
        return True
        