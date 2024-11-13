import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


gare_data = pd.read_csv("gares_ferroviaires_exploitees.csv", delimiter=';')

print(gare_data.head())

X = gare_data[['LATITUDE (WGS84)', 'LONGITUDE (WGS84)']].values
y = gare_data['NATURE'].values

print(gare_data['NATURE'].unique())

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=['LATITUDE (WGS84)', 'LONGITUDE (WGS84)'], class_names=gare_data['NATURE'].unique(), filled=True)
plt.show()
