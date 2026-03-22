class Ville:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y


def distance(ville1, ville2):
    return abs(ville1.x - ville2.x) + abs(ville1.y - ville2.y)


def afficher_ville(ville):
    print(f"Ville {ville.num}: ({ville.x}, {ville.y})")
