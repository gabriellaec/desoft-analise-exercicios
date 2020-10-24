with open("dados.csv","r") as arquivocsv:
    ler=arquivocsv.read()
    paratsv=ler.split("\t")
    with open("dados.tsv","w") as arquivostsv:
        arquivostsv.write(paratsv)