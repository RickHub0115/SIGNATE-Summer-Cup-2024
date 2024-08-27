from catboost import CatBoostClassifier
import xgboost as xgb
import lightgbm as lgb


class Model1_CatBoost_1:
    def __init__(self):
        params = {
            'scale_pos_weight': 497/(2992+497),
            'loss_function': 'Logloss',
            'eval_metric': 'AUC',
            'iterations': 7000,
            'learning_rate': 0.005,
            'depth': 3,
            # 'cat_features': category_columns,
            'l2_leaf_reg': 3,  # 3 ~ 10
            'verbose': 200,
            'random_seed': 42,
        }
        
        self.model = CatBoostClassifier(**params)

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
            self.model.fit(
                tr_x, 
                tr_y, 
                eval_set=(va_x, va_y),
                use_best_model=True
                )

    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]


class Model1_CatBoost_2:
    def __init__(self):
        params = {
            'scale_pos_weight': 497/(2992+497),
            'loss_function': 'Logloss',
            'eval_metric': 'AUC',
            'iterations': 7000,
            'learning_rate': 0.005,
            'depth': 5,
            # 'cat_features': category_columns,
            'l2_leaf_reg': 3,  # 3 ~ 10
            'verbose': 200,
            'random_seed': 42,
        }
        
        self.model = CatBoostClassifier(**params)

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
            self.model.fit(
                tr_x, 
                tr_y, 
                eval_set=(va_x, va_y),
                use_best_model=True
                )

    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]


class Model1_CatBoost_3:
    def __init__(self):
        params = {
            'scale_pos_weight': 497/(2992+497),
            'loss_function': 'Logloss',
            'eval_metric': 'AUC',
            'iterations': 7000,
            'learning_rate': 0.005,
            'depth': 7,
            # 'cat_features': category_columns,
            'l2_leaf_reg': 3,  # 3 ~ 10
            'verbose': 200,
            'random_seed': 42,
        }
        
        self.model = CatBoostClassifier(**params)

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
            self.model.fit(
                tr_x, 
                tr_y, 
                eval_set=(va_x, va_y),
                use_best_model=True
                )

    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]


class Model1_XGBoost_1:
    def __init__(self):
        params = {
            'objective': 'binary:logistic',
            'eval_metric': 'logloss',
            'num_boost_round': 5000,
            'learning_rate': 0.1,
            'max_depth': 3,
            'min_child_weight': 1,
            'gamma': 0,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'random_state': 42
        }
        
        self.params = params
        self.model = None

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        dtrain = xgb.DMatrix(tr_x, label=tr_y)
        dval = xgb.DMatrix(va_x, label=va_y)
        evals = [(dtrain, 'train'), (dval, 'eval')]
        self.model = xgb.train(
            self.params, 
            dtrain,  
            evals=evals, 
            verbose_eval=100
        )

    def predict(self, x):
        dtest = xgb.DMatrix(x)
        return self.model.predict(dtest)


class Model1_XGBoost_2:
    def __init__(self):
        params = {
            'objective': 'binary:logistic',
            'eval_metric': 'logloss',
            'num_boost_round': 5000,
            'learning_rate': 0.1,
            'max_depth': 5,
            'min_child_weight': 1,
            'gamma': 0,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'random_state': 42
        }
        
        self.params = params
        self.model = None

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        dtrain = xgb.DMatrix(tr_x, label=tr_y)
        dval = xgb.DMatrix(va_x, label=va_y)
        evals = [(dtrain, 'train'), (dval, 'eval')]
        self.model = xgb.train(
            self.params, 
            dtrain,  
            evals=evals, 
            verbose_eval=100
        )

    def predict(self, x):
        dtest = xgb.DMatrix(x)
        return self.model.predict(dtest)


class Model1_XGBoost_3:
    def __init__(self):
        params = {
            'objective': 'binary:logistic',
            'eval_metric': 'logloss',
            'num_boost_round': 5000,
            'learning_rate': 0.1,
            'max_depth': 7,
            'min_child_weight': 1,
            'gamma': 0,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'random_state': 42
        }
        
        self.params = params
        self.model = None

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        dtrain = xgb.DMatrix(tr_x, label=tr_y)
        dval = xgb.DMatrix(va_x, label=va_y)
        evals = [(dtrain, 'train'), (dval, 'eval')]
        self.model = xgb.train(
            self.params, 
            dtrain,  
            evals=evals, 
            verbose_eval=100
        )

    def predict(self, x):
        dtest = xgb.DMatrix(x)
        return self.model.predict(dtest)


class Model1_LightGBM_1:
    def __init__(self):
        params = {
            'objective': 'binary',
            'metric': 'auc',
            'learning_rate': 0.005,
            'max_depth': 3,
            'min_child_weight': 1,
            'feature_fraction': 0.8,
            'bagging_fraction': 0.8,
            'bagging_freq': 5,
            'random_state': 42,
        }
        
        self.params = params
        self.model = None

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        dtrain = lgb.Dataset(tr_x, label=tr_y)
        dval = lgb.Dataset(va_x, label=va_y, reference=dtrain)
        self.model = lgb.train(
            self.params, 
            dtrain, 
            valid_sets=[dtrain, dval],
            valid_names=['train', 'valid'],
            num_boost_rounds=7000,
            verbose_eval=100,
        )

    def predict(self, x):
        return self.model.predict(x)


class Model1_LightGBM_2:
    def __init__(self):
        params = {
            'objective': 'binary',
            'metric': 'auc',
            'learning_rate': 0.005,
            'max_depth': 5,
            'min_child_weight': 1,
            'feature_fraction': 0.8,
            'bagging_fraction': 0.8,
            'bagging_freq': 5,
            'random_state': 42,
        }
        
        self.params = params
        self.model = None

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        dtrain = lgb.Dataset(tr_x, label=tr_y)
        dval = lgb.Dataset(va_x, label=va_y, reference=dtrain)
        self.model = lgb.train(
            self.params, 
            dtrain, 
            valid_sets=[dtrain, dval],
            valid_names=['train', 'valid'],
            num_boost_rounds=7000,
            verbose_eval=100,
        )

    def predict(self, x):
        return self.model.predict(x)


class Model1_LightGBM_3:
    def __init__(self):
        params = {
            'objective': 'binary',
            'metric': 'auc',
            'learning_rate': 0.005,
            'max_depth': 7,
            'min_child_weight': 1,
            'feature_fraction': 0.8,
            'bagging_fraction': 0.8,
            'bagging_freq': 5,
            'random_state': 42,
        }
        
        self.params = params
        self.model = None

    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        dtrain = lgb.Dataset(tr_x, label=tr_y)
        dval = lgb.Dataset(va_x, label=va_y, reference=dtrain)
        self.model = lgb.train(
            self.params, 
            dtrain, 
            valid_sets=[dtrain, dval],
            valid_names=['train', 'valid'],
            num_boost_rounds=7000,
            verbose_eval=100,
        )

    def predict(self, x):
        return self.model.predict(x)