def verifica_progressao(list_n):
    if len(list_n) == 0:
        return 'NA'
    diff = list_n[1] - list_n[0]
    div = list_n[1] / list_n[0]
    for num in range(1, len(list_n)):
        if list_n[num] - list_n[num - 1] == diff:
            counter = 'PA'
        elif list_n[num] / list_n[num-1] == div:
            counter = 'PG'
        else:
            counter = 'NA'
            break
    return counter

    

    