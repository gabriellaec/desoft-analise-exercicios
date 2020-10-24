def calc_segundos(h, m, s):
    hd = 3600 * h
    md = 60 * m
    segundos = hd + md + s
    print("isso equivale a {0}".format(segundos))
    return segundos 

