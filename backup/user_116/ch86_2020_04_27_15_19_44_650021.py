with open("dados.csv","r") as arquivocsv:
    ler=arquivocsv.readlines()
    paratsv=ler.replace(",","\t")
    with open("dados.tsv","w") as arquivostsv:
        arquivostsv.write(paratsv)
