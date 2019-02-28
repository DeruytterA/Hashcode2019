def Union(list1, list2):
    final_list = list(set(list1) | set(list2))
    return final_list


def getTags(slide):
    if len(slide) == 2:
        return Union(slide[0][2:], slide[1][2:])
    return slide[0][2:]


def Verticale(V: list):
    lijst = []
    for foto in V:
        for foto2 in V:
            if foto[0] != foto2[0] and len(Union(foto[2:], foto[2:])) > (len(foto[2:]) + len(foto2[2:])) * 1.5:
                lijst.append[foto, foto2]
    return lijst

def BerekenWaarde(slide1, slide2):
    tags1 = getTags(slide1)
    tags2 = getTags(slide2)
    midden = list(set(tags1) & set(tags2))
    enkel1 = list(set(tags1) - set(tags2))
    enkel2 = list(set(tags2) - set(tags1))
    return min(len(midden), len(enkel1), len(enkel2))

def Max(H: list, lijstVerticale: list, slide):
    maximum = -1
    alleCombinaties = lijstVerticale
    gevondenMaximum = []

    #Maak lijst met alle mogelijke slides combinaties

    for i in range(len(H)):
        if not H[i][1]:
            alleCombinaties.append([H[i]])
                #zoek hoogste score in alle combinaties van slides

    for teZoeken in alleCombinaties:
        waarde = BerekenWaarde(teZoeken, slide)
        if waarde > maximum:
            maximum = waarde
            gevondenMaximum = teZoeken


            #zorg er voor dat al gebruikte fotos niet opnieuw gebruikt kunnen worden

    if len(gevondenMaximum) == 1:
        id = gevondenMaximum[0][0]
        found = False
        i = 0
        while not found:
            if H[i][0] == id:
                H[i][1] = True
                found = True
            i += 1
    else:
        for foto in gevondenMaximum:
            id = foto[0]
            found = False
            i = 0
            while not found:
                if lijstVerticale[i][0] == id:
                    lijstVerticale[i][1] = True
                    found = True
                i += 1
    return [H, lijstVerticale, gevondenMaximum]


