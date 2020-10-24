sal=15
def calcula_aumento(sal):
	if sal>1250:
		y=sal*0.1
		return y
	else:
		y=sal*0.15
		return y
print(calcula_aumento(sal))