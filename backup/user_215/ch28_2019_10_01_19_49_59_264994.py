velocidade = int(input("Insira a velocidade na qual voce estava: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Voce foi multado em R${multa:.2f}")
else:
    print("Não foi multado")