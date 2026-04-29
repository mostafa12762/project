import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
'month':['jan','feb','mar','apr','may','jun'],
'weight' : [55, 60, 65, 70, 75, 80]
})
sns.lineplot(data=data,x='month',y='weight',marker='o',color='blue')
plt.title("Weight Trend")
plt.show()
