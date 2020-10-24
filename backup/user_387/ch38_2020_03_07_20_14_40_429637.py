def quantos_uns(n):

    a = 0

    n = str(n)

    for ele in range(0, len(n)):

        if n[ele] == '1':
            a+=1

    return(a)