from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Single out data for plotting
df_versicolor = df[df['target'] == 1]

# Plot
sns.set()

bins = int(np.sqrt(df_versicolor.shape[0]))

_ = plt.hist(df_versicolor['petal length (cm)'], bins = bins)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')
plt.show()