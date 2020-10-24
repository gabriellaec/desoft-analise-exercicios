def tempo_perdido (cigarros_por_dia, tempo_fuma):
    tempo_perdido = (cigarros_por_dia * 0.00694444) * tempo_fuma
	return tempo_perdido

cigarros_por_dia = int (input ('Quantos cigarros por dia você fuma? '))
tempo_fuma = int (input('Há quantos anos você fuma? '))

print ('O seu tempo de vida perdido é {0} dias'. format (tempo_perdido (cigarros_por_dia, tempo_fuma)))