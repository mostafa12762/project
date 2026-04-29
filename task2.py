import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# قراءة ملف البيانات
df = pd.read_csv("Data.csv")

# العمود المطلوب عمل One-Hot Encoding له
column_to_encode = "Country"

# معرفة مكان العمود
col_index = df.columns.get_loc(column_to_encode)

# إنشاء Encoder
encoder = OneHotEncoder(sparse_output=False)

# تطبيق One-Hot Encoding
encoded_data = encoder.fit_transform(df[[column_to_encode]])

# تحويله إلى DataFrame
encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out([column_to_encode]),
    index=df.index
)

# حذف العمود الأصلي
df = df.drop(columns=[column_to_encode])
for i, col in enumerate(encoded_df.columns):
print(df)
df.to_csv("encoded_data.csv", index=False)