def calcula_fibonacci (n):
    i = 0
    while i <= n:
        F = F1 + F2
        F2 = F1
        F1 = F
        print (F)
n=2