def verifica_numero(n):
    soma=0
    i=0
    nl=str(n)
    list1=[int(x) for x in str(nl)]
    while i<len(list1):
        soma=soma+ list1[i]**list1[i]
        i+=1
    if soma==n:
        return 'True'
    if n<1 or soma!=n:
        return 'False'