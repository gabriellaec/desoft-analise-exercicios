def d(v,ao):
	pos = (v**2*sin(2*ao)/9.8)
	if pos < 98:
		return 'Muito perto'
	elif pos >= 98 and pos <= 102:
		return 'Acertou!'
	else:
		return 'Muito longe'