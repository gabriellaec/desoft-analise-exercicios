def interseccao_chaves(a, b):
    c = []
    keys_a = a.keys()
    keys_b = b.keys()
    for key in keys_a:
        if key in keys_b:
            c.append(key) 
    return c
    