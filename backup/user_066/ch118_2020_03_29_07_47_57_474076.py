def refelxao_total_interna(n1, n2, teta2):
    teta2 = math.radians(teta2)
    senoteta1 = n1*math.sin(teta2)/n2
    teta1 = math.asin(senoteta1)
	if senoteta1 > 1:
		return True
	else:
		return Falso