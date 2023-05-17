import pandas as pd
import matplotlib.pyplot as plt

#load the data
data = pd.read_csv('cluster_data.csv', header=0, index_col=0)
print(data)
plt.scatter(data['x'], data['y'])
plt.show()