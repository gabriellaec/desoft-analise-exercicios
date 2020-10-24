def faixa_notas(x):
    y = [0]*3
    for nota in x:
        if nota < 5:
            y[0] += nota/nota
        elif 7>= nota >=5:
            y[1] += nota/nota
        else:
            y[2] += nota/nota
    return y
            