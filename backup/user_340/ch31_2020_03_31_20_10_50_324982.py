def eh_primo(numero):
    if numero==1 or numero==0:
        return False
    elif numero==2 or numero==3:
        return True
    else:
        y=(numero%2)
        if y==0:
            return False
        if y!=0:
            i=1
            while y!=0:
                i+=2
                y=(numero%i)
                print(y)
                if y!=0:
                    return True
            if y==0:
                return False
            if i>=numero:
                    return False