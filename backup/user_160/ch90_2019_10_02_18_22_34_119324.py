def segundos_entre(hd1,hd2):
    hd1.split()
    hd2.split()
    print(sum(hd2 - hd1) for hd2, hd1 in zip(hd2, hd1))