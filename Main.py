H = []  # Horizontale foto's
V = []  # Verticale foto's
#bestand = input("Whatever het bestand is dat we willen checken: ")
bestand = "a_example.txt"
from InvoerVerwerker import leesLijn

leesLijn(H, V, bestand)

    # TODO: eerste geldige dia op True zetten
if H[0][0] < 2:
      # TODO: maak eerste dia H[0]
    H[0][1]= True
else:

    V[0][1]= True
    V[1][1]=True



