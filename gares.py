import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import plot_tree

# Charger le fichier CSV avec encodage spécifique et remplacer les virgules par des points
gare_data = pd.read_csv("gares_ferroviaires_exploitees.csv", delimiter=';', encoding="latin1")

# Remplacer les virgules par des points pour pouvoir convertir en float
gare_data['LATITUDE (WGS84)'] = gare_data['LATITUDE (WGS84)'].str.replace(',', '.').astype(float)
gare_data['LONGITUDE (WGS84)'] = gare_data['LONGITUDE (WGS84)'].str.replace(',', '.').astype(float)

# Préparer les caractéristiques (latitude et longitude) et la cible (nature)
X = gare_data[['LATITUDE (WGS84)', 'LONGITUDE (WGS84)']]
y = gare_data['NATURE']

# Remplacement des valeurs manquantes dans les caractéristiques
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Binning des catégories de la colonne 'NATURE'
# Créer un mapping manuel si nécessaire pour transformer des textes en catégories (par exemple, 'Desserte Voyageur' = 0, etc.)
nature_mapping = {
    'Desserte Voyageur': 'Low Activity',
    'Desserte Fret-Desserte Voyageur-Infrastructure': 'Moderate Activity',
    'Desserte Voyageur-Infrastructure': 'Moderate Activity',
    'Non exploitée': 'No Activity',
    'Desserte Fret-Infrastructure': 'Moderate Activity',
    'Infrastructure': 'Moderate Activity',
    'Desserte Fret': 'Low Activity',
    'Desserte Fret-Desserte Voyageur': 'High Activity'
}
y_binned = y.map(nature_mapping)

# Supprimer les valeurs cibles non mappées
y_binned = y_binned.dropna()

# Filtrer X pour correspondre aux indices de y_binned
X = X.loc[y_binned.index]

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y_binned, test_size=0.2, random_state=42)

# Créer et entraîner l'arbre de décision
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Visualisation de l'arbre de décision
plt.figure(figsize=(20, 10))
plot_tree(
    clf,
    feature_names=X.columns,
    class_names=y_binned.unique(),
    filled=True,
    rounded=True
)
plt.show()
