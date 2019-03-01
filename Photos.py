def Union(list1, list2):
    final_list = list(set(list1) | set(list2))
    return final_list


def getTags(slide):
    if len(slide) == 2:
        return Union(slide[0][2:], slide[1][2:])
    return slide[0][2:]

'''
def Verticale(V: list):
    lijst = []
    i = 0
    while i < len(V) - 1:
        if (V[i][1] is False) and (V[i + 1][1] is False):
            lijst.append([V[i], V[i + 1]])
        i += 2
    return lijst
'''

def aantalTags(foto1, foto2):
    return len(Union(foto1[2:], foto2[2:]))

def Verticale(V: list):
    lijst = []
    for i in range(len(V)):
        tussenLijst = []
        maximum = 0
        for j in range(i + 1, len(V)):
            if aantalTags(V[i], V[j]) >= maximum:
                maximum = aantalTags(V[i], V[j])
                tussenLijst = [V[i], V[j]]
        lijst.append(tussenLijst)
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
        id1 = gevondenMaximum[0][0]
        id2 = gevondenMaximum[1][0]
        for SlideInLijst in lijstVerticale:
            i = 0
            while i < len(SlideInLijst):
                if SlideInLijst[i][0] == id2:
                    SlideInLijst[i][1] = True
                if SlideInLijst[i][0] == id1:
                    SlideInLijst[i][1] = True
                i += 1
    toDelete = []
    for slide in lijstVerticale:
        if slide[0][1] and slide[1][1]:
            toDelete = slide
    if len(toDelete) > 0:
        lijstVerticale.remove(toDelete)
    return [H, lijstVerticale, gevondenMaximum]


