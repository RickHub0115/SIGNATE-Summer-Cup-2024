from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import AUC


class Model1_NN_1:
    def __init__(self):
        input_shape=62    # 特徴量の数
        
        self.model = Sequential()
        self.model.add(Dense(256, activation='relu', input_shape=(input_shape,), kernel_regularizer=l2(0.001)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=128, epochs=10):
        self.model.fit(
            tr_x,
            tr_y,
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y)
            )

    def predict(self, x):
        return self.model.predict(x).flatten()


class Model1_NN_2:
    def __init__(self):
        input_shape=62    # 特徴量の数
        
        self.model = Sequential()
        self.model.add(Dense(256, activation='relu', input_shape=(input_shape,), kernel_regularizer=l2(0.001)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.001)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=128, epochs=10):
        self.model.fit(
            tr_x,
            tr_y,
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y)
            )

    def predict(self, x):
        return self.model.predict(x).flatten()


class Model1_RNN_1:
    def __init__(self):
        input_shape=62
        units=50
        
        self.model = Sequential()
        self.model.add(LSTM(units=units, input_shape=input_shape, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=units))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=128, epochs=10):
        self.model.fit(
            tr_x, 
            tr_y,
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y))

    def predict(self, x):
        return self.model.predict(x).flatten()  # 予測確率を1次元配列で返す


class Model1DeepRNN:
    def __init__(self): 
        input_shape=62
        units=50
        
        self.model = Sequential()
        self.model.add(LSTM(units=units, input_shape=input_shape, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=units, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=units))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=64, epochs=10):
        self.model.fit(
            tr_x, 
            tr_y,
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y)
            )

    def predict(self, x):
        return self.model.predict(x).flatten()  # 予測確率を1次元配列で返す