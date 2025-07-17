
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample training data
data = {
    'temp': [40, 55, 60, 75, 30, 90],
    'current': [5, 7, 10, 15, 3, 20],
    'voltage': [220, 230, 210, 200, 240, 180],
    'fault': [0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['temp', 'current', 'voltage']]
y = df['fault']

model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, 'transformer_model.pkl')
