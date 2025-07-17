
import serial
import joblib
import numpy as np

# Load the ML model (we will train this next)
model = joblib.load('transformer_model.pkl')

# Connect to Arduino
ser = serial.Serial('COM3', 9600)  # Use correct COM port from Arduino IDE

while True:
    data = ser.readline().decode().strip()
    try:
        temp, current, voltage = map(float, data.split(','))
        features = np.array([[temp, current, voltage]])
        prediction = model.predict(features)
        if prediction[0] == 1:
            print("⚠️ Fault Detected")
        else:
            print("✅ Normal Condition")
    except:
        continue
