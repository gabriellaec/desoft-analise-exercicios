def quantos_uns(x):
	s = 0
    numero =  str(x)
    for i in numero:
        if i == 1:
            s += 1
        else:
            s += 0
    return s