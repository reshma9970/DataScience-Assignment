import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
data=sns.load_dataset('titanic')
data.head()
plt.boxplot(data.fare)
fare_data = data['fare']  # Replace 'fare' with the actual column name in your dataset

# Calculate the Z-scores for each data point
z_scores = np.abs(stats.zscore(fare_data))

# Define a threshold for identifying outliers (e.g., Z-score > 3)
threshold = 3
outlier_indices = np.where(z_scores > threshold)

# Get the actual outlier values in the 'fare' variable
outlier_values = fare_data.iloc[outlier_indices]

# Print the indices and values of outliers
print("Indices of outliers:", outlier_indices)
print("Outlier values:", outlier_values)
