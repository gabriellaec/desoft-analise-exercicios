with open("dados.csv","r") as arquivocsv:
    ler=arquivocsv.readlines()
    paratsv=ler.split("\t")
    parastring="".join(paratsv)
    with open("dados.tsv","w") as arquivostsv:
        arquivostsv.write(parastring)
