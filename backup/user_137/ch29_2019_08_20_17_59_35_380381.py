def calcula_aumento(s):
    if s > 1250:
        s *= 1.1
    if s <= 1250:
        s *= 1.15
	return s