velocidade = int(input("Qual sua velocidade? "))

def foi_multado(velocidade):
    float(velocidade)
    if velocidade > 80:
        multa = (velocidade - 80) * 5
        print("Você foi multado")
        print(f"{multa:.2f}")
    else:
        print("Não foi multado")

foi_multado(velocidade)