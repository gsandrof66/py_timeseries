import tensorflow as tf
from sklearn.base import BaseEstimator

# Custom wrapper class for Keras model
class KerasRegressorWrapper(BaseEstimator):
    def __init__(self, n_input=6, n_features=1, neurons1=50, drop1=0.1, 
                 meurons2=50, drop2=0.1, neurons3=7):
        self.model = None
        self.n_input = n_input
        self.n_features = n_features
        self.neurons1 = neurons1
        self.drop1 = drop1
        self.meurons2 = meurons2
        self.drop2 = drop2
        self.neurons3 = neurons3

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(self.n_input, self.n_features)),
            tf.keras.layers.LSTM(self.neurons1, return_sequences=True),
            tf.keras.layers.Dropout(self.drop1),
            tf.keras.layers.LSTM(self.meurons2),
            tf.keras.layers.Dropout(self.drop2),
            tf.keras.layers.Dense(self.neurons3, activation = 'relu'),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def fit(self, X, y):
        self.model = self.build_model()
        # self.model.fit(X, y, epochs=10, batch_size=32, verbose=0)
        self.model.fit(X, y, epochs=200, verbose=False, validation_split=0.1)
        return self

    def predict(self, X):
        return self.model.predict(X, verbose=False)

