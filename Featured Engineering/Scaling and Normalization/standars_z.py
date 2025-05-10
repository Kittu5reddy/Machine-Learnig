from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


data = np.array([[1, 2000], [2, 5000], [3, 10000], [4, 15000], [5, 25000]])
df = pd.DataFrame(data, columns=['Feature1', 'Feature2'])

# Apply Standardization
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)

# Convert to DataFrame
standardized_df = pd.DataFrame(standardized_data, columns=df.columns)
print(standardized_df)
