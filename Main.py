H = []  # Horizontale foto's
V = []  # Verticale foto's
#bestand = input("Whatever het bestand is dat we willen checken: ")
<<<<<<< HEAD
bestand = "c_memorable_moments.txt"
=======
bestand = "e_shiny_selfies.txt"
>>>>>>> master
from InvoerVerwerker import leesLijn
from UitvoerVerwerker import output
#from Photos import max

leesLijn(H, V, bestand)
if not H:
    V[0][1] = True
    V[1][1] = True
    eersteSlide = [V[0], V[1]]

else:
    H[0][1] = True
    eersteSlide = [H[0]]


output(V, H, eersteSlide)




