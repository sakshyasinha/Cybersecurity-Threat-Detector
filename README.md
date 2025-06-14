# 🛡️ AI Threat Detector

An AI-powered network intrusion detection system (NIDS) using the **NSL-KDD** dataset and a **Random Forest classifier**. This project demonstrates how machine learning can be used to classify network traffic as **normal** or **malicious**.

---

## 📂 Project Structure

cyber-project/
├── ai_threat_detector.py # Main training and evaluation script
├── KDDTrain+.csv # NSL-KDD training dataset
├── KDDFeatureNames.txt # Feature names for dataset columns
├── test.py # Optional test script for debugging
└── README.md # You're here!


---

## 📊 Dataset

- **NSL-KDD** is an improved version of the classic KDD Cup 1999 dataset.
- Downloaded from: https://github.com/defcom17/NSL_KDD

---

## 🧠 Model

- Uses `RandomForestClassifier` from `scikit-learn`
- Handles both **categorical** and **numerical** features
- Achieves ~**99.88% accuracy** on the training set

---

## ⚙️ Installation

### 1. Clone the repo or download the files

git clone https://github.com/your-username/cyber-project.git
cd cyber-project
2. Set up your environment
Make sure Python 3.8+ is installed, then install dependencies:


pip install -r requirements.txt
If you don't have a requirements.txt, you can install manually:


pip install pandas scikit-learn
3. Download the Dataset (if not present)

curl -O https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.csv
curl -O https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDFeatureNames.txt
