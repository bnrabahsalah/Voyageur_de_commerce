import random
from model.ville import distance


class Individu:
    def __init__(self, villes):

        chemin = villes.copy()
        random.shuffle(chemin)
        self.chemin = chemin

        self.distance_totale = self.calculer_distance_totale()
        self.fitness = (
            1 / self.distance_totale if self.distance_totale > 0 else float("inf")
        )

    def calculer_distance_totale(self):
        total = 0
        for i in range(len(self.chemin) - 1):
            total += distance(self.chemin[i], self.chemin[i + 1])
        total += distance(self.chemin[-1], self.chemin[0])
        return total
