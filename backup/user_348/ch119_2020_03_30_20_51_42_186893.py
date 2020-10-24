def fatorial(n):
    fat= 1
    conta = 1
    while conta<= n:
        fat = fat*conta
        conta = conta + 1
    return fat
def calcula_euler(x,n):
    i = 1
    e = 1
    while i<n:
        e = e+(x**i)/fatorial(i)
        i = i+1
    return e
    

        