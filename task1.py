import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data.csv')

print(df.head())
print(df.info())
print(df.describe())


plt.scatter(df['Age'], df['Salary'], color='blue', marker='o')
plt.title('Age and Salary ')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

plt.plot(df['Salary'], marker='*', linestyle='-', color='blue')
plt.title('Salary Trend Analysis (Line Plot)')
plt.ylabel('Salary')
plt.show()

sns.boxplot(x=df['Salary'], color='cyan')
plt.title('Salary Distribution and Outliers ')
plt.show()

print("  Data Issues Identified ")
missing_age = df['Age'].isnull().sum()
missing_salary = df['Salary'].isnull().sum()
print("Missing values in Age:" ,missing_age)
print("Missing values in Salary: ",missing_salary)