import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
import numpy as np
# load (downloaded if needed) the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# visualize the training data
plt.title("Sample Training Data")
for i in range(25):
    if(i == 3):
        plt.title("Sample Labeled Training Data", color = 'b')
    plt.subplot(5,5,i+1)
    plt.imshow(X_train[i], cmap=plt.get_cmap('gray'))
    plt.xlabel('Labeled: ' + str(y_train[i]), color='r')
plt.subplots_adjust(wspace=0.2,hspace=1.5)
plt.show()

# flatten 28*28 images to a 784 vector for each image
num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape((X_train.shape[0], num_pixels)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], num_pixels)).astype('float32')

# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
	model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

# build the model
model = baseline_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, batch_size=200, verbose=2)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)

# make predictions based on input images
predictions = []
for i in range(25):
    predictions.append(model.predict_classes(X_test[i].reshape(1,784)))

# visualize the final predictions
for i in range(25):
    if(i == 3):
        plt.title("Trained Prediction with a Deep Neural Network", color = 'b')
    plt.subplot(5,5,i+1)
    plt.imshow(X_test[i].reshape(28,28), cmap=plt.get_cmap('gray'))
    plt.xlabel('Labeled: ' + str(np.argmax(y_test[i])) + '/ Predicted: ' + str(predictions[i]), color='r')
plt.subplots_adjust(wspace=0.2,hspace=1.5)
plt.show()
