# Logistic Regression
from sklearn.linear_model import LogisticRegression
m1 = LogisticRegression()
m1.fit(x_train,y_train)
ypred_m1 = m1.predict(x_test)
print(ypred_m1)

# KNN
from sklearn.neighbors import KNeighborsClassifier
m2 = KNeighborsClassifier()
m2.fit(x_train, y_train)
print("Training Score", m2.score(x_train, y_train))
print("Testing Score", m2.score(x_test, y_test))
y_pred = m2.predict(x_test)
print(y_pred)

# SVM with Linear Kernel
from sklearn.svm import SVC
m3 = SVC(kernel='linear', C=100)
m3.fit(x_train, y_train)
print('Training Score', m3.score(x_train, y_train))
print('Training Score', m3.score(x_test, y_test))
ypred_m3 = m3.predict(x_test)
print('ypred\n', ypred_m3)

# SVM with rbf Kernel
m4 = SVC(kernel = 'rbf')
m4.fit(x_train, y_train)
print('Training Score', m4.score(x_train, y_train))
print('Testing Score', m4.score(x_test, y_test))
ypred_m4 = m4.predict(x_test)
print('ypred\n', ypred_m4)

