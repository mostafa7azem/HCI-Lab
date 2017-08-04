import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap

def toPairs(item1, item2, size):
    pairs = []
    for i in range(size):
        pairs.append([item1[i], item2[i]])
    return pairs

# part 1

mean1 = [37, 37]
cov = [[4, 0], [0, 4]]
size1 = 10
class1_x, class1_y = np.random.multivariate_normal(mean=mean1, cov=cov, size=size1).T

mean2 = [39, 39]
class2_x, class2_y = np.random.multivariate_normal(mean=mean2, cov=cov, size=size1).T

y11 = [1]*size1
y12 = [2]*size1
ys1 = y11 + y12
size2 = 1000
class3_x, class3_y = np.random.multivariate_normal(mean=mean2, cov=cov, size=size2).T
class4_x, class4_y = np.random.multivariate_normal(mean=mean2, cov=cov, size=size2).T

y21 = [1]*size2
y22 = [2]*size2
ys2 = y21 + y22
# part 2
lda = LinearDiscriminantAnalysis()

x1Pairs = toPairs(class1_x, class1_y, size1) + toPairs(class2_x, class2_y, size1)
x2Pairs = toPairs(class3_x, class3_y, size2) + toPairs(class4_x, class4_y, size2)
lda.fit(x1Pairs, ys1)
test1 = lda.predict(x2Pairs)

colors = ListedColormap(['#FF0000', '#0000FF'])

X1 = np.array(x1Pairs)
plt.title('LDA for 10 observations')
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.scatter(X1[:, 0], X1[:, 1], c=ys1, cmap=colors)
plt.show()

X2 = np.array(x2Pairs)
plt.title('LDA for 1000 observations')
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.scatter(X2[:, 0], X2[:, 1], c=ys2, cmap=colors)
plt.show()

print("LDA:")
for i in range(len(test1)):
    print(test1[i])

knn = KNeighborsClassifier()
knn.fit(x1Pairs, ys1)
knn.predict(x2Pairs)

print("KNN:")
for i in range(len(test1)):
    print(test1[i])
