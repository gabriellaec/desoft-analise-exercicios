def segundos_entre(hor1, hor2):
    hor1 = hor1.split(":")
    hor2 = hor2.split(":")

    hor1 = int(hor1[0]) * 3600 + int(hor1[1]) * 60 + int(hor1[2])
    hor2 = int(hor2[0]) * 3600 + int(hor2[1]) * 60 + int(hor2[2])
    return hor2 - hor1