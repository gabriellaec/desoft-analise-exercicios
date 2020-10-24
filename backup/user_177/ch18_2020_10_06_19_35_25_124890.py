def testa_maioridade(idade):
     if idade >= 21:
         return 'Liberado EUA e Brasil'
     else:
         if idade >= 18:
             return ' Liberado Brasil'
         else:
             return 'Não está liberado'

print(testa_maioridade(17))
print(testa_maioridade(20))
print(testa_maioridade(21))

        
