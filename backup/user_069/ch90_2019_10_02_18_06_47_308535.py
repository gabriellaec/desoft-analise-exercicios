def segundos_entre (t1, t2):
    t1 = [h1, m1, s1]
    t2 = [h2, m2, s2]
    d = (h1*3600 + m1*60 + s1) - (h2*3600 + m2*60 + s2)
    return abs(d)