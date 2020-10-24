def aniversariantes_de_setembro(DICI):
    final={}
    for c in DICI:
        if (DICI[c])[4]==9:
            final[c]=DICI[c]
    return final
