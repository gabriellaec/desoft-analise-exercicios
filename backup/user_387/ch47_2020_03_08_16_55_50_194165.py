def estritamente_crescente(a):

    b = a
    c = []
    a = a[::-1]

    for i in range(len(a)):
        for j in range(i + 1, len(a)):

            if a[i] <= a[j]:
                c.append(a[i])

    for val in c:
        b.remove(val)

    return(b)