def leesLijn(H, V, bestand):
    with open(bestand) as f:
        aantalFotos = int(f.readline())
        for fotoID in range(aantalFotos):
            lijn = f.readline()
            lijnlijst = (lijn[:-1].split(" "))
            lijnlijst[1] = False
            lijnlijst = [fotoID] + lijnlijst
            if lijnlijst[1] == "H":
                H.append([lijnlijst[0]] + lijnlijst[2:])
            else:
                V.append([lijnlijst[0]] + lijnlijst[2:])
    f.close()






