def estritamente_crescente(x):
    if len(x) == 0:
        return x
    i = len(x)
    j = 1
    y = [0]
    y[0] = x[0]
    m = x[0]
    while j < i:
        if x[j] > m:
            y.append(x[j])
            m = x[j]
        j += 1         
    return y