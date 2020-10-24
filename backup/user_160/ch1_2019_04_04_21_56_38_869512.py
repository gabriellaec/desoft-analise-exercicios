def calcula_valor_devido (valemp,nummes,txjuros):
    valortotal = valemp + (valemp*txjuros)**nummes
    return valortotal
