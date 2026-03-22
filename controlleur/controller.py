import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import random
import threading
from model.ville import Ville
from model.genetic_algorithm import GeneticAlgorithm
from model.individu import Individu


class Controller:
    def __init__(self, view):
        self.view = view
        self.villes = []

    def generer_villes(self, n, width, height):
        margin = 30
        self.villes = [
            Ville(
                i,
                random.randint(margin, width - margin),
                random.randint(margin, height - margin),
            )
            for i in range(n)
        ]
        self.view.dessiner(self.villes)
        self.view.reset_stats()

    def lancer(self, taille_pop):
        if not self.villes:
            return
        self.view.set_boutons(False)
        self.view.lbl_status.config(text="En cours...")

        def run():
            algo = GeneticAlgorithm(self.villes, taille_pop)

            for gen in range(100):
                if len(algo.population.liste) < 2:
                    break

                enfants = []
                while len(enfants) < taille_pop:
                    parent1, parent2 = algo.selection()
                    child_chemin = algo.crossover(parent1, parent2)
                    child_chemin = algo.mutation(child_chemin)

                    enfant = Individu(child_chemin)
                    enfant.chemin = child_chemin.copy()
                    enfant.distance_totale = enfant.calculer_distance_totale()
                    enfant.fitness = 1 / enfant.distance_totale

                    enfants.append(enfant)

                algo.population.liste = enfants
                best = algo.population.get_best()

                def update(g=gen, b=best):
                    self.view.dessiner(self.villes, b.chemin, "blue")
                    self.view.lbl_gen.config(text=f"Génération : {g + 1}")
                    self.view.lbl_dist.config(
                        text=f"Distance : {b.distance_totale:.1f}"
                    )
                    self.view.progress["value"] = g + 1

                self.view.root.after(0, update)

                # pause courte pour rendre visible l'évolution
                import time

                time.sleep(0.02)

            best = algo.population.get_best()

            def finish(b=best):
                self.view.dessiner(self.villes, b.chemin, "green")
                self.view.lbl_gen.config(text=f"Génération : {min(100, gen + 1)}")
                self.view.lbl_dist.config(text=f"Distance : {b.distance_totale:.1f}")
                self.view.progress["value"] = min(100, gen + 1)
                self.view.lbl_status.config(text="Terminé ✔")
                self.view.set_boutons(True)

            self.view.root.after(0, finish)

        threading.Thread(target=run, daemon=True).start()

    def reset(self):
        self.villes = []
        self.view.canvas.delete("all")
        self.view.reset_stats()
        self.view.set_boutons(True)
