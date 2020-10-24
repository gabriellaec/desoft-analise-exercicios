def eh_bissexto(ano):
  if ano%4==0 & ano%100 != 0:
    print("é bissexto")
  elif ano%4 != 0 & ano%100 != 0 &ano%400 == 0:
    print("é bissexto")
  else: print("não é bissexto")
y = eh_bissexto

ano = int(input("defina o ano\n"))
y(ano)

    
        