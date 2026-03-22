🧬 Voyageur de Commerce – Algorithme Génétique (TSP)
📌 Description

Ce projet a pour objectif de résoudre le problème du voyageur de commerce (TSP) en utilisant un algorithme génétique.
Le but est de trouver le chemin le plus court permettant de passer par toutes les villes une seule fois et de revenir au point de départ.

Une interface graphique en Tkinter permet de générer des villes aléatoires et de visualiser le chemin trouvé par l’algorithme.

🧠 Algorithme génétique

L’algorithme génétique simule l’évolution naturelle pour améliorer progressivement les solutions.

Étapes de l’algorithme :
Génération d’une population initiale aléatoire
Évaluation de la fitness de chaque individu
Sélection des meilleurs individus
Croisement (crossover)
Mutation
Création d’une nouvelle population
Répétition jusqu’à amélioration de la solution

La fitness est définie par :

fitness = 1 / distance_totale

Plus la distance est petite, plus la fitness est grande.

🏗 Architecture MVC

Le projet est organisé selon l’architecture MVC (Model - View - Controller) :

project/
│
├── model/
│   ├── ville.py
│   ├── individu.py
│   ├── population.py
│   └── genetic_algorithm.py
│
├── view/
│   └── interface.py
│
├── controller/
│   └── controller.py
│
└── main.py
Partie	Rôle
Model	Algorithme génétique et structures de données
View	Interface graphique Tkinter
Controller	Lien entre l’interface et l’algorithme
main	Lance l’application
🖥 Interface graphique

L’interface permet :

Entrer le nombre de villes
Générer des villes aléatoires
Lancer l’algorithme génétique
Afficher le chemin trouvé

Les villes sont représentées par des points et le chemin par des lignes.

▶️ Lancer le projet

Dans le terminal :

python main.py
Utilisation :
Entrer le nombre de villes
Cliquer sur Générer villes
Cliquer sur Lancer algorithme
Le chemin optimal s’affiche
⚙️ Paramètres de l’algorithme
Paramètre	Valeur
Taille population	50
Nombre de générations	100
Mutation	Échange de deux villes
Sélection	Meilleurs individus
Crossover	Order crossover
📚 Projet réalisé dans le cadre du cours

Intelligence Artificielle – Algorithmes Génétique
Problème du Voyageur de Commerce (TSP)

👤 Auteur

Rayane Ait Braham
Salah Benrabah
Lina Ouallam