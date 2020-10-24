def verifica_numero(n):
    soma=0
    i=0
    list1=[str.split(n)]
    while i<len(list1):
        soma=soma+ list1[i]**list1[i]
        i+=1
    if soma==n:
        return 'True'
    if n<1 or soma!=n:
        return 'False'