lista = []

def maior_primo_menor_que(n):
    for num in range(2, n + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    lista.append(num)
    return lista
                


x = maior_primo_menor_que()
p = x[-2]
print(p)
