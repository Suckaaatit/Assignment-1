# -*- coding: utf-8 -*-
"""Untitled0.ipynb

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# --- Step 1 & 2: Load, Clean, and Prepare Data ---

# Load the dataset
try:
    df = pd.read_csv('load_data.csv')
except FileNotFoundError:
    print("Error: 'load_data.csv' not found. Please make sure the file is in the correct directory.")
    exit()

# Clean column names by replacing special characters with '_'
df.columns = df.columns.str.strip().str.replace('[^A-Za-z0-9]+', '_', regex=True).str.lower()

# Convert 'date_time' column, ensuring day comes first
df['date_time'] = pd.to_datetime(df['date_time'], dayfirst=True)

# Feature Engineering
df['hour'] = df['date_time'].dt.hour
df['dayofweek'] = df['date_time'].dt.dayofweek
df['month'] = df['date_time'].dt.month

# Sort dataframe by date
df = df.sort_values(by='date_time').reset_index(drop=True)

# Encode the target variable
le = LabelEncoder()
df['load_type_encoded'] = le.fit_transform(df['load_type'])
load_type_mapping = {index: label for index, label in enumerate(le.classes_)}

print("--- Data Preparation Summary ---")
print("Load Type Mapping:", load_type_mapping)
print("Cleaned Column Names:", df.columns.tolist())
print("\n")

# --- Step 3: Data Splitting (Time-Based) ---
last_month = df['date_time'].dt.month.iloc[-1]
last_year = df['date_time'].dt.year.iloc[-1]
split_date = df[(df['date_time'].dt.month == last_month) & (df['date_time'].dt.year == last_year)]['date_time'].min()

train_df = df[df['date_time'] < split_date]
test_df = df[df['date_time'] >= split_date]

print("--- Data Splitting Summary ---")
print(f"Training data runs from {train_df['date_time'].min()} to {train_df['date_time'].max()}")
print(f"Test data runs from {test_df['date_time'].min()} to {test_df['date_time'].max()}")
print("\n")

# THIS IS THE FINAL, ROBUST FIX:
# Dynamically create the list of features instead of hardcoding it.
non_feature_cols = ['date_time', 'load_type', 'load_type_encoded']
features = [col for col in df.columns if col not in non_feature_cols]
target = 'load_type_encoded'

print("--- Features Used for Training ---")
print(features)
print("\n")


X_train = train_df[features]
y_train = train_df[target]
X_test = test_df[features]
y_test = test_df[target]

# --- FIX: Add this right before the model training loop ---
# This ensures any and all missing values are filled.
X_train = X_train.fillna(X_train.median())
X_test = X_test.fillna(X_test.median())


# --- Step 4 & 5: Model Training and Evaluation ---
models = {
    "Logistic Regression": LogisticRegression(max_iter=2000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100)
}

results = {}

# This loop will now work correctly
for model_name, model in models.items():
    print(f"--- Training and Evaluating: {model_name} ---")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=le.classes_, zero_division=0)

    results[model_name] = {
        "accuracy": accuracy,
        "classification_report": report
    }

    print(f"Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)
    print("\n")

# --- Conclusion ---
best_model_name = max(results, key=lambda k: results[k]['accuracy'])
print(f"--- Final Conclusion ---")
print(f"The best performing model is the '{best_model_name}' with an accuracy of {results[best_model_name]['accuracy']:.4f}.")

