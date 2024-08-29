from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import AUC
import tensorflow as tf
import torch
from pytorch_tabnet.tab_model import TabNetClassifier


class Model1_NN_1:
    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(Dense(256, activation='relu', input_shape=(input_shape,), kernel_regularizer=l2(0.001)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=128, epochs=10):
        self.model.fit(
            tr_x,
            tr_y,
            #class_weight={0: 2992, 1: 497},
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y),
            )

    def predict(self, x):
        return self.model.predict(x).flatten()


class Model1_NN_2:
    def __init__(self, input_shape):        
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
            #class_weight={0: 2992, 1: 497},
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y)
            )

    def predict(self, x):
        return self.model.predict(x).flatten()


class Model1_NN_all_1:
    def __init__(self, input_shape=62):
        self.model = Sequential()
        self.model.add(Dense(256, activation='relu', input_shape=(input_shape,)))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=128, epochs=10):
        self.model.fit(
            tr_x,
            tr_y,
            #class_weight={0: 2992, 1: 497},
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y)
            )

    def predict(self, x):
        return self.model.predict(x).flatten()


class Model1_NN_all_2:
    def __init__(self, input_shape=62):
        self.model = Sequential()
        self.model.add(Dense(256, activation='relu', input_shape=(input_shape,)))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=[AUC()])

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, batch_size=128, epochs=10):
        self.model.fit(
            tr_x,
            tr_y,
            #class_weight={0: 2992, 1: 497},
            batch_size=batch_size,
            epochs=epochs, 
            verbose=1,
            validation_data=(va_x, va_y)
            )

    def predict(self, x):
        return self.model.predict(x).flatten()


class Model1_TabNet_1:
    def __init__(self, input_dim, output_dim=1):
        """
        :param input_dim: 入力データの特徴量数
        :param output_dim: 出力ユニット数（通常は1）
        """
        self.model = TabNetClassifier(
            input_dim=input_dim,
            output_dim=output_dim,
            n_d=8,  # デシジョン層のフィーチャー数
            n_a=8,  # Attention層のフィーチャー数
            n_steps=3,  # シーケンシャルに実行されるステップの数
            gamma=1.3,  # FeatureReusageの制御パラメータ
            lambda_sparse=1e-3,  # スパース正則化の強度
            optimizer_fn=torch.optim.Adam,
            optimizer_params=dict(lr=2e-2),
            scheduler_params={"step_size":10, "gamma":0.9},
            scheduler_fn=torch.optim.lr_scheduler.StepLR,
            mask_type='entmax'  # "sparsemax" または "entmax"
        )

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, max_epochs=50, batch_size=1024, virtual_batch_size=128):
        tr_x = tr_x.values
        tr_y = tr_y.values
        va_x = va_x.values if va_x is not None else None
        va_y = va_y.values if va_y is not None else None
        
        self.model.fit(
            X_train=tr_x, y_train=tr_y,
            eval_set=[(va_x, va_y)] if va_x is not None and va_y is not None else [],
            max_epochs=max_epochs,
            patience=10,
            batch_size=batch_size, 
            virtual_batch_size=virtual_batch_size,
            num_workers=0,
            drop_last=False
        )

    def predict(self, x):
        return self.model.predict_proba(x.values)[:, 1]


class Model1_TabNet_2:
    def __init__(self, input_dim, output_dim=1):
        """
        :param input_dim: 入力データの特徴量数
        :param output_dim: 出力ユニット数（通常は1）
        """
        self.model = TabNetClassifier(
            input_dim=input_dim,
            output_dim=output_dim,
            n_d=32,  # デシジョン層のフィーチャー数（深いモデルのために大きめに設定）
            n_a=32,  # Attention層のフィーチャー数
            n_steps=5,  # ステップ数を増やしてモデルを深く
            gamma=1.5,  # FeatureReusageの制御パラメータ
            lambda_sparse=1e-3,  # スパース正則化の強度
            optimizer_fn=torch.optim.Adam,
            optimizer_params=dict(lr=2e-2),
            scheduler_params={"step_size":10, "gamma":0.9},
            scheduler_fn=torch.optim.lr_scheduler.StepLR,
            mask_type='entmax'  # "sparsemax" または "entmax"
        )

    def fit(self, tr_x, tr_y, va_x=None, va_y=None, max_epochs=100, batch_size=1024, virtual_batch_size=128):
        tr_x = tr_x.values
        tr_y = tr_y.values
        va_x = va_x.values if va_x is not None else None
        va_y = va_y.values if va_y is not None else None
        
        self.model.fit(
            X_train=tr_x, y_train=tr_y,
            eval_set=[(va_x, va_y)] if va_x is not None and va_y is not None else [],
            max_epochs=max_epochs,
            patience=15,
            batch_size=batch_size, 
            virtual_batch_size=virtual_batch_size,
            num_workers=0,
            drop_last=False
        )

    def predict(self, x):
        return self.model.predict_proba(x.values)[:, 1]