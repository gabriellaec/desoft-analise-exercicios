def segundos_entre(a,b):
    c = a.split(":")
    d = b.split(":")
    total_a = int(c[0])*60*60 + int(c[1])*60 + int(c[2])
    total_b = int(d[0])*60*60 + int(d[1])*60+ int(d[2])
    return total_b - total_a

