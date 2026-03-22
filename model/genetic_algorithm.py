from model.population import Population, Individu
import random


class GeneticAlgorithm:
    def __init__(self, villes, taille_population):
        self.taille_population = taille_population
        self.population = Population(villes, taille_population)

    def selection(self):
        self.population.order_by_fitness()
        parent1 = self.population.liste[-1]
        parent2 = self.population.liste[-2]
        return parent1, parent2

    def crossover(self, parent1, parent2):
        if random.random() < 0.7:
            child_chemin = parent1.chemin[: len(parent1.chemin) // 2]

            for ville in parent2.chemin:
                if ville not in child_chemin:
                    child_chemin.append(ville)
        else:
            child_chemin = (
                parent1.chemin if parent1.fitness > parent2.fitness else parent2.chemin
            )

        return child_chemin

    def mutation(self, child_chemin):
        if random.random() < 0.3:
            i = random.randint(0, len(child_chemin) - 1)
            j = random.randint(0, len(child_chemin) - 1)
            child_chemin[i], child_chemin[j] = child_chemin[j], child_chemin[i]
        return child_chemin

    def new_population(self, child_chemin):
        while len(self.population.liste) < self.population.taille_population:
            new_individu = Individu(child_chemin)
            self.population.liste.append(new_individu)
            self.population.order_by_fitness()
            self.population.liste.pop(0)  # Supprimer le moins performant

    def run(self):
        new_pop = self.population
        for _ in range(100):
            pop = new_pop
            enfants = []
            while len(enfants) < self.taille_population:
                parent1, parent2 = self.selection()
                child_chemin = self.crossover(parent1, parent2)
                child_chemin = self.mutation(child_chemin)

                enfant = Individu(child_chemin)
                enfant.chemin = child_chemin.copy()
                enfant.distance_totale = enfant.calculer_distance_totale()
                enfant.fitness = 1 / enfant.distance_totale

                enfants.append(enfant)
                new_pop.liste = enfants
                if new_pop.get_best().fitness > self.population.get_best().fitness:
                    break
        self.population = new_pop
        return self.population.get_best()
