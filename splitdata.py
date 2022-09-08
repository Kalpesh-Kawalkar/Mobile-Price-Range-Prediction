# For Logistic Regression
x = df[['battery_power', 'int_memory', 'pc', 'clock_speed']]
y = df['price_range']
print(type(x))
print(type(y))
x.head()
y.head()

from sklearn.model_selection import train_test_split
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
x_train.head()

# For KNN
x = df.iloc[:,:-1]
y = df.iloc[:,-1]
print(type(x))
print(type(y))
print(x.shape)
print(y.shape)
x.head()
y.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# For SVM
x = df.iloc[:, :-1]
y = df.iloc[:, -1]
print(x.shape)
print(y.shape)
print(type(x), type(y))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
