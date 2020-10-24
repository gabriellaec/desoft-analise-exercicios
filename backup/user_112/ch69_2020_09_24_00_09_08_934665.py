def junta_listas(n):
    x = len(n)
    i = 0
    junta = []
    while i < x:
        junta = junta + n[i]
        i = i + 1
    return (junta)