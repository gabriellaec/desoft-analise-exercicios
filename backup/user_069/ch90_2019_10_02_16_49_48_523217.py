def segundos_entre (t1, t2):
    d = abs((t1[0]*3600 + t1[2]*60 + t1[2]) - (t2[0]*3600 + t2[2]*60 + t2[2]))
    return d