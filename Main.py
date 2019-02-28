H = []  # Horizontale foto's
V = []  # Verticale foto's
#bestand = input("Whatever het bestand is dat we willen checken: ")
bestand = "c_memorable_moments.txt"
from InvoerVerwerker import leesLijn
from UitvoerVerwerker import output
#from Photos import max

leesLijn(H, V, bestand)
eersteSlide = [H[0]]
eersteSlide[0][1] = True

output(V, H, eersteSlide)




