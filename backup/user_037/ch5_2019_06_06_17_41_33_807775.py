lista = []
def pre(m):
    for num in range(2, m + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    lista.append(num)
    return lista
                

def maior_primo_menor_que(n):
    x = pre(n)
    p = x[-2]
    return p

print(maior_primo_menor_que(10))