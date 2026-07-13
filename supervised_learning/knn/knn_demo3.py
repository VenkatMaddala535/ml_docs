from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

marks = [[35,40,67],[34,76,45],[12,100,67],[67,45,89],[89,78,56],[34,34,34],[38,35,39],[40,45,98],[21,31,43]]
result =["pass","fail","fail","pass","pass","fail","pass","pass","fail"]

obj = KNeighborsClassifier(n_neighbors=3)
obj.fit(marks,result)

prediction1 = obj.predict([[34,100,100]])
print(prediction1)

prediction2 = obj.predict([[35,100,100]])
print(prediction2)

actual_values  = result
predicted_values = obj.predict(marks)
accuracy = accuracy_score(actual_values,predicted_values)
print(accuracy)
