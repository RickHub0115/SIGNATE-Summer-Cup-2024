from sklearn.linear_model import LogisticRegression

class Model1_Logistic:
    def __init__(self):
        self.model = LogisticRegression(
            C=1.0,
            solver='liblinear',
            max_iter=300
        )
    
    def fit(self, tr_x, tr_y, va_x=None, va_y=None):
        self.model.fit(tr_x, tr_y)
    
    def predict(self, x):
        return self.model.predict_proba(x)[:, 1]