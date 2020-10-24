def segundos_entre (t1, t2):
    s1 = t1[0]*3600 + t1[1]*60 + t1[2]
    s2 = t2[0]*3600 + t2[1]*60 + t2[2]
    d = abs(s1 - s2)
    return d