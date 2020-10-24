def eh_primo(x):
    if x%2==0:
          return False
    elif x==0 or x==1:
        return False
    elif x==2:
        return True
    else:
        y=3
        while (y<x):
            if x%y==0:
                break 
            y=y+2
        if y==x:
            return True 
        else:
            return False