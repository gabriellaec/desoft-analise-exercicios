cigarros_por_dia = input ('Quantos cigarros por dia você fuma? ')
tempo_fuma = ('Há quantos anos você fuma? ')

def tempo_perdido (cigarros_por_dia, tempo_fuma):
    tempo_perdido = (cigarros_por_dia * 0.00694444) * tempo_fuma
	return tempo_perdido
print ('O seu tempo de vida perdido é {0} dias'. format (tempo_perdido))