a = [1, 2, 3, 4]
num_elementos = len(a)

def soma_valores(s):
    i = 0
    s = 0
	while i<num_elementos:
        s += a[i]
        i += 1
    return s