def testando_idades(idade):
	if idade<=11:
        return'crianca'
    elif idade>=12 and idade<=17:
        return'adolescente'
    else:
        return'adulto'
print(testando_idades(16))