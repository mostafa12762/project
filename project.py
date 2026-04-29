import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Load dataset
df_original = pd.read_csv("Data.csv")

# Detect columns
numerical_cols = df_original.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df_original.select_dtypes(include=['object']).columns

def apply_imputation(df, method):
    df_result = df.copy()
    if len(categorical_cols) > 0:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df_result[categorical_cols] = cat_imputer.fit_transform(df_result[categorical_cols])
    
    
    if method == "simple":
        imputer = SimpleImputer(strategy='mean')
    elif method == "knn":
        imputer = KNNImputer(n_neighbors=5)
    elif method == "iterative":
        imputer = IterativeImputer(random_state=42)
        
    df_result[numerical_cols] = imputer.fit_transform(df_result[numerical_cols])
    return df_result

methods = ["simple", "knn", "iterative"]

for method in methods:
    # Process
    print(f"Applying {method} imputation...")
    final_df = apply_imputation(df_original, method)
    filename = f"{method}_output.csv"
    final_df.to_csv(filename, index=False)
    print(f"Saved: {filename}")

print("\nAll tasks completed successfully.")