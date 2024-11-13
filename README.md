***Analyse des Gares Ferroviaires avec un Arbre de Décision***
Ce projet utilise un modèle d’arbre de décision pour analyser la nature des gares ferroviaires exploitées en France, en fonction de leurs coordonnées géographiques (latitude et longitude). Le modèle de machine learning, implémenté avec Scikit-Learn, est visualisé pour mieux comprendre la classification des gares.

**Structure du Projet**
gares_ferroviaires_exploitees.csv : Le fichier de données CSV contenant les informations sur les gares ferroviaires.
gares.py : Script Python principal pour charger les données, entraîner un arbre de décision, et visualiser le modèle.
README.md : Ce fichier, expliquant le projet, les étapes d'installation, et l'exécution.
Prérequis
Pour exécuter ce projet, les éléments suivants sont nécessaires :

Python 3.7+
Packages Python :
pandas
scikit-learn
matplotlib
Installation des dépendances
Utilisez pip pour installer les dépendances nécessaires executer sur votre terminal de commandes:

pip install pandas scikit-learn matplotlib

**Jeu de Données**
Le fichier gares_ferroviaires_exploitees.csv contient les informations des gares, notamment :

CODE_LIGNE : Code de la ligne de chemin de fer
NOM : Nom de la gare
NATURE : Nature de la gare (par exemple, desserte voyageurs, fret)
LATITUDE (WGS84) et LONGITUDE (WGS84) : Coordonnées géographiques de la gare
Remarque : Assurez-vous que ce fichier est placé dans le même répertoire que le script Python.

Exécution du Script
Pour exécuter le script, assurez-vous que gares.py et gares_ferroviaires_exploitees.csv se trouvent dans le même répertoire, puis lancez sur le terminal de commandes:

python gares.py

**Le script effectue les actions suivantes**

Chargement des données : Lit les données de gares.csv en utilisant pandas.
Préparation des données : Sélectionne la latitude et la longitude comme caractéristiques (X) et la nature de la gare comme étiquette cible (y).
Entraînement de l’arbre de décision : Utilise Scikit-Learn pour entraîner un modèle d’arbre de décision.
Visualisation : Affiche l’arbre de décision avec matplotlib, montrant comment le modèle utilise les coordonnées géographiques pour classer les gares.
Exemple d'Usage
Le script affichera en sortie les premières lignes du jeu de données, les classes de NATURE présentes, ainsi que la visualisation de l’arbre de décision permettant d’interpréter le modèle.

**Résultats Attendues**
L'arbre de décision prédit la nature d'une gare en fonction de sa localisation géographique. Cette analyse permet d'identifier des tendances dans la distribution géographique des types de gares.