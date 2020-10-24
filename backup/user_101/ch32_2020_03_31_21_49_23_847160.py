def avalia_primo(num):
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

def primos_entre(a, b):
    todos_num = range(a, b+1)
    i_todos = 0
    primos =[]
    while i_todos < len(todos_num):
        if avalia_primo(todos_num[i_todos]) == True:
            primos.append(todos_num[i_todos])
        i_todos += 1
    return primos

def lista_primos(n):
    novo = n*10
    primos_ate_n = primos_entre(0, novo)
    primos = primos_ate_n[0:n]
    return primos
