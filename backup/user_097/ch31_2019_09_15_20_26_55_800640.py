def valor_emprestimo(v, s, a):
    ps = (0.3*s)
    pm = (v/a)
    if (pm<=ps):
        return ("Empréstimo aprovado")
    elif (pm>ps):
        return ("Empréstimo não aprovado")