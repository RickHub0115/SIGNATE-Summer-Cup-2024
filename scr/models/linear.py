from sklearn.linear_model import LogisticRegression

class Model1_Logistic_1:
    def __init__(self):
        self.model = LogisticRegression(
            class_weight='balanced',
            C=1.0,
            solver='liblinear',
            max_iter=300
        )
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]

class Model1_Logistic_2:
    def __init__(self):
        self.model = LogisticRegression(
            class_weight='balanced',
            C=0.1,
            solver='liblinear',
            max_iter=300
        )
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]

class Model1_Logistic_3:
    def __init__(self):
        self.model = LogisticRegression(
            class_weight='balanced',
            C=0.01,
            solver='liblinear',
            max_iter=300
        )
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]

class Model1_Logistic_4:
    def __init__(self):
        self.model = LogisticRegression(
            class_weight='balanced',
            C=0.001,
            solver='liblinear',
            max_iter=300
        )
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]

class Model2_Logistic:
    def __init__(self):
        self.model = LogisticRegression(
            #class_weight='balanced',
            C=1.0,
            solver='liblinear',
            max_iter=300
        )
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]