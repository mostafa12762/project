import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
   'Height': [160, 165, 170, 175, 180, 185],
    'Weight': [55, 60, 65, 70, 75, 80],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F']
})
sns.scatterplot(data=data,x='Height',y='Weight',hue='Gender',style='Gender')
plt.title("Height")
plt.show()
