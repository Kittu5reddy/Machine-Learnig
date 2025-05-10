from sklearn.preprocessing import RobustScaler
import pandas as pd
import numpy as np


data = np.array([[1, 2000], [2, 5000], [3, 10000], [4, 15000], [5, 25000]])
df = pd.DataFrame(data, columns=['Feature1', 'Feature2'])

# Apply Robust Scaling
scaler = RobustScaler()
robust_scaled_data = scaler.fit_transform(df)

# Convert to DataFrame
robust_scaled_df = pd.DataFrame(robust_scaled_data, columns=df.columns)
print(robust_scaled_df)
