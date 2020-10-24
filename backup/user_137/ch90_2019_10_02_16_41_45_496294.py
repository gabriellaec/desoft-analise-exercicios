def segundos_entre(h1, h2):
    h1 = h1.split(':')
    h2 = h2.split(':')
    r1 = (int(h1[0]) * 3600) + (int(h1[1]) * 60) + int(h1[2])
    r2 = (int(h2[0]) * 3600) + (int(h2[1]) * 60) + int(h2[2])
    return r2 - r1