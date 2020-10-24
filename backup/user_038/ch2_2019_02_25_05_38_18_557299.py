def calcula_velocidade_media(distancia, tempo):
    v_media = distancia/tempo
    print("A velocidade media do veiculo é: {0}km/h".format(v_media))
d = float(input("Qual a distancia percorrida em km? "))
t = float(input("Qual foi o tempo, em horas, demorado? "))
calcula_velocidade_media(d, t)