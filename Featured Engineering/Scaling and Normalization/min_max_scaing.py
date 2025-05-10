from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

# Sample data
data = np.array([[1, 2000], [2, 5000], [3, 10000], [4, 15000], [5, 25000]])
df = pd.DataFrame(data, columns=['Feature1', 'Feature2'])

# Apply Min-Max Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

# Convert to DataFrame for better readability
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df)
