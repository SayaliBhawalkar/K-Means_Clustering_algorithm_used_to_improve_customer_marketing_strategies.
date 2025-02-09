import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# generate data set
np.random.seed(42)
data = {'AnnualIncome': np.random.randint(30000,100000,100),
        'SpendingScore' : np.random.randint(1,100,100)}
df = pd.DataFrame(data)
print(df)

plt.scatter(df['AnnualIncome'], df['SpendingScore'])
plt.title('Customer Data - Annual income vs spending score')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

a = df.values
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster']= KMeans.fit_predict(a)

print(df)
