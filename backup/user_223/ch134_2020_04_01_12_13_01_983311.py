def verifica_quadrado_perfeito(n):
	m = n
	i = 0
	while m >= 0:
		m = n-(2+i)
		i += 2
		return m
		m_quad = m**2
		if m_quad == n:
			return (True)
			print ("True")
		else:
			return (False)
			print ("False")