def multa(velocidade):
    if velocidade>80 :
        d = velocidade - 80
        m = d*5        
        print("Você foi multado em  {0:.2f} ." .format(m))
    elif velocidade <=80:
        print("Não foi multado")
velo = float(input("Entre com a velocidade do carro: "))
multa(velo)