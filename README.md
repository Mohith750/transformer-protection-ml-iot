# ⚡ IoT-Based Transformer Protection Using Machine Learning

This project protects electrical transformers using real-time sensor data and machine learning algorithms. It predicts transformer faults in advance and avoids damage.

---

## 🚀 Features

- Real-time monitoring of temperature, voltage, and current
- Arduino + sensors to collect live data
- Python ML model to predict faults
- Alerts if unsafe conditions are detected

---

## 🛠 Tech Stack

- Arduino UNO
- DHT11 sensor, Current Sensor, Voltage divider
- Python, scikit-learn, pandas, joblib
- Serial communication (USB)
- Optional: ThinkSpeak / Blynk for cloud dashboard

---

## 📁 Project Files
---

## ▶ How to Run

### 1. Train ML Model

```bash
python ml_model_training.py
Upload to Arduino

Use Arduino IDE

Upload arduino_code.ino


3. Start Live Monitor

python live_monitoring.py


---

📷 Sample Output

Temp: 60°C | Current: 10A | Voltage: 210V
Prediction: ⚠ Fault Detected


---

📚 Learning Outcome

Real-time data acquisition

Sensor integration (hardware + software)

Machine learning fault prediction

IoT + EEE + Python integration



---

✅ Future Improvements

Add GSM/email alerts

Cloud dashboard with live data

Train model on more real transformer data
