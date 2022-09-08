# For Logistic Regression
from sklearn.metrics import confusion_matrix,classification_report
cm = confusion_matrix(y_test,ypred_m1)
print(cm)
print(classification_report(y_test, ypred_m1))

# For KNN
from sklearn.metrics import confusion_matrix,classification_report
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

# For SVM linear kernel
cm_m3 = confusion_matrix(y_test, ypred_m3)
print(cm_m3)
print(classification_report(y_test, ypred_m3))

# For SVM rbf kernel
cm_m4 = confusion_matrix(y_test, ypred_m4)
print(cm_m4)
print(classification_report(y_test, ypred_m4))

## 1) SVM with Linear kernel - Accuracy = 98 per cent
## 2) SVM with Rbf kernel - Accuracy = 97 per cent
## So,it turns out that SVM model is suitable for the given dataset.