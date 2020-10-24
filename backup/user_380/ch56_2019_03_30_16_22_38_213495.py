def calcula_total_da_nota(nota):
    total = 0
    if len(nota) > 0:
        for i in range(len(nota[0])):
            total += nota[0]*nota[1]
    return total