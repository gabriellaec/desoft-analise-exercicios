def multador(placa,velmax,dist,ti,tf):
    dt = tf-ti
    vel = dist / dt 

    if vel>velmax:
        if vel< (1.2*velmax):
            multa = 130.16
            infracao = "Média"
            penalidade = "multa de R${0}".format(multa)

            return placa,infracao, multa, penalidade

        elif vel> (1.2*velmax) and vel<(1.5*velmax):
            multa = 195.23
            infracao = "Grave"
            penalidade = "multa de R${0}".format(multa)

            return placa,infracao, multa, penalidade
        
        elif vel>(1.5*velmax):
            multa = 3*195.23
            infracao = "Gravíssima"
            penalidade = ("multa de R${0}, suspensão imediata do direito de dirigir e apreensão do documento de habilitação".format(multa))

            return placa,infracao, multa, penalidade

    if vel<=velmax:

        return "não ultrapassou o limite de velocidade, portanto não há multa ou penalidade a ser aplicada"

placa = str(input("Qual a placa do carro?: "))
velmax = int(input("QUal a velocidade máxima permitida na via?: "))
dist = float(input("Qual a distancia entre as cameras na via?: "))

while placa!="":
    
   
    ti = float(input("Qual o instante de tempo em que o veículo passa pela primeira camera?: "))
    tf = float(input("Qual o instante de tempo em que o veículo passa pela segunda camera?: "))

    print(multador(placa,velmax,dist,ti,tf))

    placa = str(input("Qual a placa do carro?: "))