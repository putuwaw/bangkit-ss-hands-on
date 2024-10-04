import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import keras

iris = load_iris()
X = iris.data
y = iris.target
print(iris.target_names)

encoder = LabelBinarizer()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

inputs = keras.Input(shape=(4,))
x = keras.layers.Dense(10, activation="relu")(inputs)
x = keras.layers.Dense(10, activation="relu")(x)
outputs = keras.layers.Dense(3, activation="softmax")(x)
model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, epochs=25, batch_size=5, validation_split=0.1, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {accuracy:.4f}")

model.save("model/iris.keras")
