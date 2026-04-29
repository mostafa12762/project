import matplotlib.pyplot as plt
height = [160, 165, 170, 175, 180, 185]
weight = [55, 60, 65, 70, 75, 80]
plt.scatter(height,weight,color='blue',marker='*')
plt.xlabel('height(cm)')
plt.ylabel('weight(kg)')
plt.title("Height vs Weight")
plt.grid(True)
plt.show();