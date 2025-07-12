#  Assignment-1 — Power Load Prediction  
*USEREADY*

This project is a classic classification task aimed at predicting the **load type on a power grid** — either **LIGHT**, **MEDIUM**, or **MAXIMUM LOAD** — based on historical energy usage and environmental data.

It covers the **end-to-end data science workflow**, from data preprocessing to feature engineering and model evaluation.

---

##  Project Objective

The goal was to build a machine learning model that classifies power grid load types using features like:

- Energy usage (KWh)
- Reactive power (lagging/leading)
- CO₂ levels
- Time-based features (hour, day, month)

---

##  The Dataset

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

### 1.  Data Preprocessing

- Renamed inconsistent column headers
- Filled missing values:
  - **Numerical**: Median
  - **Categorical**: Mode

### 2.  Feature Engineering

From the `DATE_TIME` field, the following were extracted:

- `HOUR` — hour of the day
- `DAYOFWEEK` — day of the week (0 = Monday)
- `MONTH` — numeric month

### 3.  Train/Test Split

- Used the **last month** of the dataset as the **test set**
- Remaining data used for **training**

This time-based split simulates a real-world future prediction scenario.

### 4.  Model Training & Evaluation

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
 Results

Logistic Regression
<img width="338" height="169" alt="image" src="https://github.com/user-attachments/assets/f319156b-601d-4202-a6fb-58fefdaf7379" />

Decision Tree
<img width="335" height="174" alt="image" src="https://github.com/user-attachments/assets/a19e8a52-face-4d57-a0f8-4bad9e975877" />

Random Forest
<img width="353" height="164" alt="image" src="https://github.com/user-attachments/assets/4ee08a97-7085-4ae7-a3b0-54825968d245" />

This is the result and it tells us that Random Forest is the best among all three alogs used


