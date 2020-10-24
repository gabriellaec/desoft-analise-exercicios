def verifica_quadrado_perfeito(n):
	m = n
	i = 0
	while m >= 0:
		m = n-(2+i)
		i += 2
		return m

		if m**2 == n:
			return True
		else:
			return False