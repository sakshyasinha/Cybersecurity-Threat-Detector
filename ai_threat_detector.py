import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

print("Loading dataset...")

# Step 1: Load feature names
with open("KDDFeatureNames.txt", "r") as f:
    feature_names = [line.strip().split(":")[0] for line in f.readlines()]

# Append 'label' and 'difficulty' column (as in the dataset)
feature_names.append("label")
feature_names.append("difficulty")

# Step 2: Load the dataset
df = pd.read_csv("KDDTrain+.csv", names=feature_names)

# Step 3: Drop the 'difficulty' column
df.drop("difficulty", axis=1, inplace=True)

# Step 4: One-hot encode categorical features (protocol_type, service, flag)
df = pd.get_dummies(df, columns=["protocol_type", "service", "flag"])

# Step 5: Convert label to binary (0 = normal, 1 = attack)
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

# Step 6: Ensure all columns are numeric (clean weird data)
df = df.apply(pd.to_numeric, errors='coerce')

# Step 7: Drop any rows with NaNs (after cleaning)
df.dropna(inplace=True)

# Step 8: Split features and target
X = df.drop("label", axis=1)
y = df["label"]

# Step 9: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 10: Train the model
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 11: Evaluate
y_pred = model.predict(X_test)

print("Model Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
