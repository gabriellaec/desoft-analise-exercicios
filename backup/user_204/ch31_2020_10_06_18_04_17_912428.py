def eh_primo(numero):
    step_1 = numero % 2
    if step_1 == 0 :
        return False
    i = 1
    while i <= numero:
        eq = numero % i
        if eq == 0:
            return False