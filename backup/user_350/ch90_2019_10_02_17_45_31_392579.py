def segundos_entre(a,b):
    total_a = a[0]*60*60 + a[1]*60 + a[2]
    total_b = b[0]*60*60 + b[1]*60+ b[2]
    return total_b - total_a