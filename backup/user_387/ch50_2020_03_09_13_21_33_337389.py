def junta_nome_sobrenome(a, b):

    c = []

    for num in range(len(a)):
        c.insert(num, a[num] + ' ' + b[num])

    return(c)
  