def PiWallis(n_arg):
    soma = 1
    num_p = 2
    num_i = 1
    for i in range(n_arg + 1):
        soma *= num_p/num_i
        if i % 2 == 0:
            num_p += 2
        else:
            num_i += 2
    soma = soma *2
    return soma