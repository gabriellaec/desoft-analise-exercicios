def calcula_valor_devido(valor,meses,juros):
    v_final= valor*(1+juros)**meses
    return v_final