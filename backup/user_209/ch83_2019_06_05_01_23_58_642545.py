dic = {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
def medias_por_inicial (dic):
    dicnovo = {}
    for nome,media in dic.items ():
        inicial = nome[0]
        dicnovo[inicial] = media
    return dicnovo