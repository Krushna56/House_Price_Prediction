"""
Simple Linear Regression implementation from scratch
"""

class LinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None
    
    def _normalize(self, X):
        """Normalize features to have zero mean and unit variance"""
        means = [sum(col) / len(col) for col in zip(*X)]
        stds = [
            (sum((x - mean) ** 2 for x in col) / len(col)) ** 0.5
            for col, mean in zip(zip(*X), means)
        ]
        
        normalized = [
            [(x - mean) / std for x, mean, std in zip(row, means, stds)]
            for row in X
        ]
        return normalized, means, stds
    
    def fit(self, X, y, learning_rate=0.01, epochs=1000):
        """Train the model using gradient descent"""
        # Normalize features
        X_norm, self.means, self.stds = self._normalize(X)
        n_samples = len(X)
        n_features = len(X[0])
        
        # Initialize parameters
        self.weights = [0] * n_features
        self.bias = 0
        
        # Gradient descent
        for _ in range(epochs):
            # Compute predictions
            y_pred = [
                sum(w * x for w, x in zip(self.weights, x_i)) + self.bias
                for x_i in X_norm
            ]
            
            # Compute gradients
            dw = [0] * n_features
            db = 0
            for i in range(n_samples):
                error = y_pred[i] - y[i]
                for j in range(n_features):
                    dw[j] += error * X_norm[i][j]
                db += error
            
            # Update parameters
            self.weights = [
                w - (learning_rate * dw_i / n_samples)
                for w, dw_i in zip(self.weights, dw)
            ]
            self.bias -= learning_rate * db / n_samples
    
    def predict(self, X):
        """Make predictions for new data"""
        # Normalize input features
        X_norm = [
            [(x - mean) / std for x, mean, std in zip(row, self.means, self.stds)]
            for row in X
        ]
        
        # Make predictions
        return [
            sum(w * x for w, x in zip(self.weights, x_i)) + self.bias
            for x_i in X_norm
        ]