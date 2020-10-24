A = int(input("Escolha um ano: "))

def eh_bissexto(A):
    
    if A%400 == 0:
        return(True)
    if A%4 == 0 and A%100 != 0:
        return(False)
    else:
        return(False)

print(eh_bissexto(A))