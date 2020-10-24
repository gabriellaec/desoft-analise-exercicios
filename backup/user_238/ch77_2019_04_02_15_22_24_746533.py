def calcula_tempo(atletas):
    v={}
    for e in atletas:
        v[e]=atletas[e]*0.2
    return v
atletas={'a': 8, 'b':12,'c':15}
print(calcula_tempo(atletas))

