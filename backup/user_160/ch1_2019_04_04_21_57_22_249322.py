def calcula_valor_devido (valemp,nummes,txjuros):
    valemp != 0
    nummes != 0 
    txjuros != 0
    valortotal = valemp + (valemp*txjuros)**nummes
    return valortotal
