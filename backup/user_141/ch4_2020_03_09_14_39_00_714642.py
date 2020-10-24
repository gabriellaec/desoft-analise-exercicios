def testando_idades(idade)
	if idade<=11:
        return('crianca')
    elif idade>=12 and idade<=17:
        return('adolescente')
print(testando_idades(16))