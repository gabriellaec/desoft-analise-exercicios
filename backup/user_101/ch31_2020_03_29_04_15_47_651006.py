def eh_primo(num):
    impar = 3
    semResto = []
    if num % 2 == 0 and num != 2 or num == 1 or num ==0:
        return False
    elif num == 2 or num == 3:
        return True
    while num > impar:
        if num % impar == 0:
            semResto.append(impar)
        impar += 2
    if len(semResto) == 0:
        return True
    return False