import random
import string

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.utils import to_categorical
from tensorflow.keras import layers, models
train = pd.read_csv('../images/model/sign_mnist_train.csv')
test = pd.read_csv('../images/model/sign_mnist_test.csv')

train_data = np.array(train, dtype='float32')
test_data = np.array(test, dtype='float32')

class_names = list(string.ascii_lowercase[:26].replace('z', ''))

X_train = train_data[:, 1:] / 255
X_test = test_data[:, 1:] / 255

y_train = train_data[:, 0]
y_train_cat = to_categorical(y_train, num_classes=25)

y_test = test_data[:, 0]
y_test_cat = to_categorical(y_test, num_classes=25)

X_train = X_train.reshape(X_train.shape[0], *(28, 28, 1))
X_test = X_test.reshape(X_test.shape[0], *(28, 28, 1))
def create_model():


    # print(X_train.shape)
    # print(X_test.shape)

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(25, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    model.fit(X_train, y_train_cat, batch_size=128, epochs=10, validation_data=(X_test, y_test_cat))

    loss, accuracy = model.evaluate(X_test, y_test_cat)
    # print(f"Loss: {loss}")
    # print(f"Accuracy: {accuracy}")
    model.save('sign_language_classification.keras')

def get_model():
    model = models.load_model('image_classification.keras')
    return model

model = models.load_model('sign_language_classification.keras')
prediction = model.evaluate(X_test)
i = random.randint(1, len(prediction))
plt.imshow(X_test[i, :, :, 0])
print('Prediction: ', class_names[int(prediction[i])])
print('True: ', class_names[int(y_test[i])])
