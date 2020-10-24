ve=10
nm=10
tx=10/100
def calcula_valor_devido(valor_emprestado, numero_de_meses, taxa_de_juros):
  valor_emprestdo=ve
  numero_de_meses=nm
  taxa_de_jurus=tx
  vt=ve*(1+tx)**nm
  return vt
print (calcula_valor_devido)