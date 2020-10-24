def eh_primo(num):
    i = 3
    if num == 0:
        return "False"
    if num == 1:
        return "False"
    if num == 2:
        return "True"
    if num == 3:
        return "True"
    while i < num:
        if num%2 == 0: 
            return "False"           
        if num%i !=  0:
            i = i +1
            return "True"
        if num%i == 0:
            i = i+1
            return"False"
            