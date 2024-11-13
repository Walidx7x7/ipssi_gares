import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Charger le fichier CSV avec encodage spécifique et remplacer les virgules par des points
gare_data = pd.read_csv("gares_ferroviaires_exploitees.csv", delimiter=';', encoding="latin1")

# Remplacer les virgules par des points pour pouvoir convertir en float
gare_data['LATITUDE (WGS84)'] = gare_data['LATITUDE (WGS84)'].str.replace(',', '.').astype(float)
gare_data['LONGITUDE (WGS84)'] = gare_data['LONGITUDE (WGS84)'].str.replace(',', '.').astype(float)

# Préparer les caractéristiques (latitude et longitude) et la cible (nature)
X = gare_data[['LATITUDE (WGS84)', 'LONGITUDE (WGS84)']].values
y = gare_data['NATURE'].values

# Afficher les catégories uniques de la colonne 'NATURE'
print(gare_data['NATURE'].unique())

# Initialiser et entraîner l'arbre de décision
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
print("test")
# Visualisation de l'arbre de décision
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=['LATITUDE (WGS84)', 'LONGITUDE (WGS84)'], class_names=gare_data['NATURE'].unique(), filled=True)
plt.show()
