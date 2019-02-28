def Union(list1, list2):
    final_list = list(set(list1) | set(list2))
    return final_list


def getTags(slide):
    if len(slide) == 2:
        return Union(slide[0][2:], slide[1][2:])
    return slide[0][2:]


def BerekenWaarde(slide1, slide2):
    tags1 = getTags(slide1)
    tags2 = getTags(slide2)
    midden = list(set(tags1) & set(tags2))
    enkel1 = list(set(tags1) - set(tags2))
    enkel2 = list(set(tags2) - set(tags1))
    return min(len(midden), len(enkel1), len(enkel2))


def Max(H: list, V: list, slide):
    maximum = -1
    alleCombinaties = []
    gevondenMaximum = []
    for i in range(len(H)):
        if not H[i][1]:
            alleCombinaties.append([H[i]])
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if not V[i][1] and not V[j][1]:
                dezeSlide = [V[i], V[j]]
                alleCombinaties.append(dezeSlide)
    for teZoeken in alleCombinaties:
        waarde = BerekenWaarde(teZoeken, slide)
        if waarde > maximum:
            maximum = waarde
            gevondenMaximum = teZoeken
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
                    if V[i][0] == id:
                        V[i][1] = True
                        found = True
                    i += 1
    return [H, V, gevondenMaximum]
