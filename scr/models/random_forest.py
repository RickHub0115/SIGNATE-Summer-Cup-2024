from sklearn.ensemble import RandomForestClassifier

# 決定木の深さが「浅い」
class Model1_RandomForest_1:
    def __init__(self):
        params = {
            'class_weight': 'balanced',
            'criterion': 'gini',
            'n_estimators': 500,
            'max_depth': 3,
            'min_samples_split': 2,
            'min_samples_leaf': 1,
            'max_features': 'sqrt',
            'bootstrap': True,
            'random_state': 42
            }
        
        self.model = RandomForestClassifier(**params)
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]

# 決定木の深さが「深い」
class Model1_RandomForest_2:
    def __init__(self):
        params = {
            'class_weight': 'balanced',
            'criterion': 'gini',
            'n_estimators': 500,
            'max_depth': 5,
            'min_samples_split': 2,
            'min_samples_leaf': 1,
            'max_features': 'sqrt',
            'bootstrap': True,
            'random_state': 42
            }
        
        self.model = RandomForestClassifier(**params)
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]

class Model1_RandomForest_3:
    def __init__(self):
        params = {
            'class_weight': 'balanced',
            'criterion': 'gini',
            'n_estimators': 500,
            'max_depth': 7,
            'min_samples_split': 2,
            'min_samples_leaf': 1,
            'max_features': 'sqrt',
            'bootstrap': True,
            'random_state': 42
            }
        
        self.model = RandomForestClassifier(**params)
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]