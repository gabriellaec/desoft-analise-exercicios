def eh_bissexto(ano):
    if ano%4==0 and ano%100!=0 or ano%400==0:
        return ("Ano Bissexto")
    else:
        return ("Não é um ano Bissexto!")