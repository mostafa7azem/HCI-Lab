import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#Generate datasets
X, y = datasets.make_classification(n_samples=50, n_classes=2, n_features=4)

iris = datasets.load_iris()
#X = iris.data
#y = iris.target
print(X)
print(y)
print(len(X[0]))
print(len(X))
print(len(y))

lda = LinearDiscriminantAnalysis()

X_r = lda.fit(X, y).transform(X)
print(X_r[0])

colors = ['red', 'blue', 'green','black', 'yellow', 'gray']
plt.figure()
for color, i in zip(colors, [0, 1]):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], alpha=.8, color=color)

plt.title('LDA')
plt.show()
