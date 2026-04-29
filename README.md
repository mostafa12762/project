# 🧠 Data Imputation Project

## 📌 Simple Explanation

This project is used to handle missing values in a dataset using different imputation techniques in Python.

---

## ⚙️ What the code does

- Reads a dataset from a CSV file (`Data.csv`)
- Detects numerical and categorical columns automatically
- Fills missing values in categorical columns using the most frequent value
- Applies different methods to handle missing values in numerical columns:
  - Simple Imputation (Mean)
  - KNN Imputation (based on nearest neighbors)
  - Iterative Imputation (prediction-based method)
- Saves a new cleaned dataset for each method separately

---

## 🔄 Imputation Methods Used

### 1. Simple Imputation
Replaces missing numerical values with the average (mean).

### 2. KNN Imputation
Uses similar data points (nearest neighbors) to estimate missing values.

### 3. Iterative Imputation
Predicts missing values using machine learning models.

---

## 📁 Output Files

After running the script, it generates:

- simple_output.csv
- knn_output.csv
- iterative_output.csv

---

## 🎯 Purpose

The goal is to compare different ways of handling missing data and see how each method affects the dataset.

---

## 👨‍💻 Note

Make sure `Data.csv` is in the same folder before running the code.
