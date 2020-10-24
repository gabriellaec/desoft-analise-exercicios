def interseccao_chaves(a, b):
    c = []
    values_a = a.values()
    values_b = b.values()
    for value in values_a:
        if value in values_b:
            c.append(value) 
    return c