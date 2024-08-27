from catboost import CatBoostClassifier

# 決定木の深さが「浅い」モデル
class Model1_CatBoost_1:
    def __init__(self):
        params = {
            'scale_pos_weight': 497/(2992+497),
            'loss_function': 'Logloss',
            'eval_metric': 'AUC',
            'iterations': 5000,
            'learning_rate': 0.005,
            'depth': 3,
            # 'cat_features': category_columns,
            'l2_leaf_reg': 5,  # 3 ~ 10
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

# 決定木の深さが「普通」モデル
class Model1_CatBoost_2:
    def __init__(self):
        params = {
            'scale_pos_weight': 497/(2992+497),
            'loss_function': 'Logloss',
            'eval_metric': 'AUC',
            'iterations': 5000,
            'learning_rate': 0.005,
            'depth': 5,
            # 'cat_features': category_columns,
            'l2_leaf_reg': 5,  # 3 ~ 10
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

# 決定木の深さが「深い」モデル
class Model1_CatBoost_3:
    def __init__(self):
        params = {
            'scale_pos_weight': 497/(2992+497),
            'loss_function': 'Logloss',
            'eval_metric': 'AUC',
            'iterations': 5000,
            'learning_rate': 0.005,
            'depth': 7,
            # 'cat_features': category_columns,
            'l2_leaf_reg': 5,  # 3 ~ 10
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