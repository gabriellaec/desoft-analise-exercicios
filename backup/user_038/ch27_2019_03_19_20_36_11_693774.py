def expec_vida_fumante(cigarros_dia, tempo_fumante):
    x = int(10*cigarros_dia*365/24)
    print(x)
expec_vida_fumante(int(input("Quantos cigarros voce fuma por dia? ")),
                   int(input("Há quantos anos voce fuma? ")))