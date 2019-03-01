def output(V, H, eersteSlide):
    from Photos import Max
    from Photos import Verticale
    lijstVerticale = Verticale(V)
    aantalSlides = len(H) + len(lijstVerticale)
    resultaat = open("resultaatB.txt", "w+")
    resultaat.write(str(aantalSlides) + "\n")
    resultaat.write(str(eersteSlide[0][0]) + "\n")
    for teller in range(1, aantalSlides):
        maxOutput = Max(H, lijstVerticale, eersteSlide)
        H = maxOutput[0]
        lijstVerticale = maxOutput[1]
        if len(maxOutput[2]) == 2:
            resultaat.write(str(maxOutput[2][0][0]) + " " + str(maxOutput[2][1][0]) + "\n")
        else:
            resultaat.write(str(maxOutput[2][0][0]) + "\n")
