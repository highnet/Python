import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# load the iris dataset
data_train = pd.read_csv('./iris.csv')

# the 3 classification classes are replaced in the data set by the numerical
# values 0,1 and 2
data_train.loc[data_train['species']=='Iris-setosa', 'species']=0
data_train.loc[data_train['species']=='Iris-versicolor', 'species']=1
data_train.loc[data_train['species']=='Iris-virginica', 'species']=2
data_train = data_train.apply(pd.to_numeric)

# the data set is transformed into a matrix
data_train_array = data_train.as_matrix()
print ('---data_train_array')
print (data_train_array)
print ('---')

# the data set is split into two categories, training data
# and testing data. 80% of the data is used for training
# and 20% of the data is used for testing the model.
X_train, X_test, y_train, y_test = train_test_split(data_train_array[:,:4],
                                                    data_train_array[:,4],
                                                    test_size = 0.2)

print ('---X_train')
print (X_train)
print ('---X_test')
print (X_test)
print ('---y_train')
print (y_train)
print ('---y_test')
print (y_test)
print ('---')

# A neural network is used for classification (multi layer perceptron)
# with input layer with 4 neurons representing sepal length, sepal width,
# petal length and petal width
# a hidden layer with 10 neurons
# an outputlayer with 4 neurons representing the classes

mlp = MLPClassifier(hidden_layer_sizes=(10,),activation='relu', solver=
'adam', max_iter=350, batch_size=10, verbose=True)

# the neural network is trained with the dataset
mlp.fit(X_train,y_train)

# the results are printed
print("Training result:  %5.3f" % mlp.score(X_train, y_train))

# the model is tested with the test dataset
predictions = mlp.predict(X_test)
# the confusion matrix is printed
print(confusion_matrix(y_test,predictions))
# from the confusion matrix, precision, recall and f1 score are calculated
print(classification_report(y_test,predictions))

# the model is tested and results are printed
print("Test Result: %5.3f" % mlp.score(X_test,y_test))

# print the value weights for each layer
print("WEIGHTS:",mlp.coefs_)
print("BIASES:", mlp.intercepts_)

# now we can make our own predictions.
print(mlp.predict([[5.1,3.5,1.4,0.2],[5.9,3.,5.1,1.8],[4.9,3.,1.4,0.2],[5.8,2.7,4.1,1.]]))

# the loss-curve is visualized in the file Plot_of_loss_values.png
loss_values = mlp.loss_curve_
plt.plot(loss_values)
plt.savefig("./Plot_of_loss_values.png")
plt.show()
