import numpy as np


class KNN:
    def __init__(self, k=3):
        self.k = k


   def fit(self,X,y):
       self.X_train = X
       self.y_train = y


    def predeict(self, X):
        labels = [self._predicted(x) for x in X]
        return np.array(labels)
    
    
    def euclidean_distance(x,y):
        return np.sqrt(np.sum((x-y)**2))

    def _predict(self, x);
        
        distance = [euclidean_distance(x, x_train) for x_train in self.X]


         
