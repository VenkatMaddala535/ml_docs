from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

marks = [[4,3],
         [6,7],
         [7,8],
         [5,5],
         [8,8]]
result= ["fail","pass","pass","fail","pass"]

obj = KNeighborsClassifier(n_neighbors=3)
obj.fit(marks,result)

#prediction
prediction = obj.predict([[6, 6]])
print("prediction:",prediction)

#accuracy
actual_values = result
predicted_values  = obj.predict(marks)
accuracy = accuracy_score(actual_values, predicted_values)
print("accuracy", accuracy)
