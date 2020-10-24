def primos_entre (a,b):
    i = 3
    n = a
    contagem = 0
    while n < b:
        if n == 2:
            primo = True
        elif n == 1 or n == 0:
            primo = False
        elif(n%2==0):
            primo = False
        else:
            while (i<n):
                if (n%i==0):
                    primo = False
                    break
                else:
                    i = i+2
            primo = True
        if primo == True:
            contagem += 1
        n += 1
    return contagem
    