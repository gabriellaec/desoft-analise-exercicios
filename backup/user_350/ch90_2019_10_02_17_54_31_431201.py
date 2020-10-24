def segundos_entre(a,b):
    c = a.split(":")
    d = b.split(":")
    total_a = c[0]*60*60 + c[1]*60 + c[2]
    total_b = d[0]*60*60 + d[1]*60+ d[2]
    return total_b - total_a

