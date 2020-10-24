sal=1300
def calcula_aumento(sal):
	if sal>1250:
		y=sal*1.1
		return y
	else:
		y=sal*1.15
		return y
print(calcula_aumento(sal))