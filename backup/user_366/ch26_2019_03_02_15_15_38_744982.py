pergunta_dias = int(input('Diga um numero de dias'));
pergunta_h = int(input('Diga um numero de horas'));
pergunta_min = int(input('Diga um numero de minutos'));
pergunta_s = int(input('Diga um numero de segundos'));

total_s = 86400*pergunta_dias + 3600*pergunta_h + 60*pergunta_min + pergunta_s
print(total_s)