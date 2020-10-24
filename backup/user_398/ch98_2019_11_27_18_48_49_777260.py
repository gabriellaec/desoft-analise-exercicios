def bairro_mais_custoso(ano):
     gastos = total_do_semestre_por_bairro(ano)
     maior=0
     bairro_mais_caro=' '
     for bairro in gastos:
         if gastos[bairro]>maior:
             maior=gastos[bairro]
             bairro_mais_caro=bairro
     return bairro_mais_caro