def eh_primo(x):
    i = 1
    while i <= x:
        if x%2==0 or x%(x-i)==0:
            return("True")
        else:
            return("False")