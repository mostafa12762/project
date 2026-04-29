import matplotlib.pyplot as plt
month=['jan','feb','mar','apr','may','jun']
weight = [55, 60, 65, 70, 75, 80]
plt.plot(month,weight,color='blue',marker='o',linestyle='-',linewidth=2)
plt.xlabel('Month')
plt.ylabel('Weight (kg)')
plt.title("Weight Trend")
plt.grid(True)
plt.show();