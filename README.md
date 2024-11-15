Projet d'Analyse des Gares Ferroviaires avec un Arbre de Décision
Ce projet utilise un arbre de décision pour analyser et classer les gares ferroviaires françaises selon leur latitude, longitude et nature d'exploitation. Les étapes incluent le prétraitement des données, l'imputation des valeurs manquantes, la transformation des valeurs de NATURE en catégories, et l'entraînement d'un modèle de classification.

Fichiers
gares_ferroviaires_exploitees.csv : Fichier de données source contenant les informations des gares, y compris leur latitude, longitude, et nature.
gares.py : Script Python principal pour le chargement des données, le prétraitement et l'entraînement du modèle de décision.
Prérequis
Python 3.7+
Bibliothèques Python :
pandas
scikit-learn
matplotlib
Pour installer les bibliothèques requises, exécutez :

bash
Copier le code
pip install pandas scikit-learn matplotlib
Description des Étapes
Chargement des Données : Le fichier CSV gares_ferroviaires_exploitees.csv est chargé avec l'encodage latin1, et les virgules dans les colonnes de latitude et longitude sont remplacées par des points pour assurer un formatage numérique correct.

Préparation des Données :

Les colonnes LATITUDE (WGS84) et LONGITUDE (WGS84) sont converties en float après le remplacement des virgules.
Les valeurs manquantes dans ces colonnes sont remplies par la moyenne (SimpleImputer avec la stratégie mean).
Binning de la Colonne NATURE :

La colonne NATURE (qui décrit le type de service de chaque gare) est transformée en catégories plus générales (ex : Low Activity, Moderate Activity, etc.).
Cette étape est réalisée à l'aide d'un dictionnaire de mapping pour regrouper les types de gares en classes.
Division des Données :

Les données sont divisées en ensembles d'entraînement et de test avec une proportion de 80%-20%.
Entraînement et Visualisation de l'Arbre de Décision :

Un arbre de décision est entraîné sur les données d'entraînement. La profondeur de l'arbre est limitée à 3 pour éviter le sur-apprentissage et assurer une visualisation plus claire.
L'arbre de décision est ensuite affiché avec les caractéristiques (LATITUDE et LONGITUDE) et les classes de NATURE binées.
Utilisation
Pour exécuter le script et visualiser l'arbre de décision, lancez :

bash
Copier le code
python gares.py
Ce script affiche un arbre de décision illustrant les relations géographiques entre les gares et leur nature d'exploitation.

Exemple de Sortie
Le script produit une visualisation de l'arbre de décision où chaque nœud représente une décision basée sur les caractéristiques géographiques des gares et indique les catégories de NATURE.

Notes
Les modifications incluent la gestion des données manquantes et la simplification des catégories de NATURE en classes binées pour améliorer la lisibilité de l'arbre.
La profondeur de l'arbre a été réduite pour éviter le sur-ajustement et faciliter l'interprétation visuelle.
Ce README vous offre une vue d'ensemble des étapes du projet, des méthodes de prétraitement et des paramètres utilisés dans le modèle d'arbre de décision.
