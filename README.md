# ⚡ Assignment-1 — Power Load Prediction  
*USEREADY*

This project is a classic classification task aimed at predicting the **load type on a power grid** — either **LIGHT**, **MEDIUM**, or **MAXIMUM LOAD** — based on historical energy usage and environmental data.

It covers the **end-to-end data science workflow**, from data preprocessing to feature engineering and model evaluation.

---

## 🎯 Project Objective

The goal was to build a machine learning model that classifies power grid load types using features like:

- Energy usage (KWh)
- Reactive power (lagging/leading)
- CO₂ levels
- Time-based features (hour, day, month)

---

## 📂 The Dataset

Filename: `LOAD_DATA.CSV`  
The dataset includes the following key columns:

| Column Name                               | Description                              |
|-------------------------------------------|------------------------------------------|
| `DATE_TIME`                               | Timestamp of the reading                 |
| `USAGE_KWH`                               | Energy usage in kilowatt-hours           |
| `LAGGING_CURRENT_REACTIVE_POWER_KVARH`    | Lagging reactive power                   |
| `LEADING_CURRENT_REACTIVE_POWER_KVARH`    | Leading reactive power                   |
| `CO2(PPM)`                                | CO₂ levels in parts per million          |
| `NSM`                                     | Seconds from midnight                    |
| `LOAD_TYPE`                               | Target class: LIGHT / MEDIUM / MAXIMUM   |

---

## 🔧 How It Works

### 1. 🧹 Data Preprocessing

- Renamed inconsistent column headers
- Filled missing values:
  - **Numerical**: Median
  - **Categorical**: Mode

### 2. 🛠 Feature Engineering

From the `DATE_TIME` field, the following were extracted:

- `HOUR` — hour of the day
- `DAYOFWEEK` — day of the week (0 = Monday)
- `MONTH` — numeric month

### 3. 🧪 Train/Test Split

- Used the **last month** of the dataset as the **test set**
- Remaining data used for **training**

This time-based split simulates a real-world future prediction scenario.

### 4. 🤖 Model Training & Evaluation

Tested the following models:

- **Logistic Regression**
- **Decision Tree**
- **Random Forest**

Metrics used:

- Accuracy
- Precision
- Recall
- F1-Score

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install pandas scikit-learn

2. Run the code
Place LOAD_DATA.CSV in the project directory and run the Python script or Jupyter Notebook.

The output includes model performance reports for all classifiers.

📊 Results
Logistic Regression
<img width="479" height="248" alt="image" src="https://github.com/user-attachments/assets/c94c19ee-097f-4b86-bf81-d9b432657852" />
Decision Tree
<img width="367" height="191" alt="image" src="https://github.com/user-attachments/assets/0c1b94de-e49d-4833-8d22-41d79bb37987" />
Random Forest
<img width="350" height="166" alt="image" src="https://github.com/user-attachments/assets/af66aa19-d6c3-4b21-bc17-3e08e36416e8" />
This is the result for Random Forest



