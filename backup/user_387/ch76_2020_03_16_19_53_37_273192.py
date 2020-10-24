def aniversariantes_de_setembro(a):
    for pessoa in list(a):
        if ((a[pessoa])[3:5]) != '09':
            del a[pessoa]
    return a
    