from sklearn.neighbors import KNeighborsClassifier

marks = [[30],[35],[40],[80],[85],[90]]
result = ["fail","fail","fail","pass","pass","pass"]

obj = KNeighborsClassifier(n_neighbors=3)

obj.fit(marks, result)

prediction = obj.predict([[60.4]])

print(prediction)
