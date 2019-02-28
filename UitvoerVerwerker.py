def output(V, H, eersteSlide):
    from Photos import Max
    aantalSlides = len(H) + len(V) // 2
    resultaat = open("resultaat.txt", "w+")
    resultaat.write(str(aantalSlides) + "\n")
    resultaat.write(str(eersteSlide[0][0]) + "\n")
    for teller in range(1, aantalSlides):
        maxOutput = Max(H, V, eersteSlide)
        H = maxOutput[0]
        V = maxOutput[1]
        if len(maxOutput[2]) == 2:
            resultaat.write(str(maxOutput[2][0][0]) + " " + str(maxOutput[2][1][0]) + "\n")
        else:
            resultaat.write(str(maxOutput[2][0][0]) + "\n")
