def verifica_numero (n):
    n = (n**n)/n
    sn = (n**n)/n+(n**n)/n+(n**n)/n
    if n < 1 or n != sn:
        print('false')
    else:
        print('true')
return (n)