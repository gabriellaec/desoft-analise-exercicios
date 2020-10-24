def função(c, s, q):
    p = c/(q/12)
    if p <= 0.3*s:
        return'Empréstimo aprovado'
    else:
        return'Empréstimo não aprovado'