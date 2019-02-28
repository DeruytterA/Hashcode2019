def Union(list1, list2):
    final_list = list(set(list1) | set(list2))
    return final_list


def Max(H: list, V, slide):
    if len(slide) == 2:
        huidigeTags = Union(slide[0][2:], slide[1][2:])
    else:
        huidigeTags = slide[0][2:]
    maximum = 0
    alleCombinaties = H         #array van slides
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            dezeSlide = [i, j]
            alleCombinaties.append(dezeSlide)