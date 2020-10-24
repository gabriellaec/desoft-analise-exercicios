import math
def calcula_euler(listae):
    listae = [0]*n
    listae[0] = 1
    listae[1] = x
    i = 2
    while i < n:
        listae[i] = (x/i)*listae[i-1]
        i += 1
    return sum(listae)