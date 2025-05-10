import numpy as np
import pandas as pd
import numpy as np


data = np.array([[1, 2000], [2, 5000], [3, 10000], [4, 15000], [5, 25000]])
df = pd.DataFrame(data, columns=['Feature1', 'Feature2'])

# Apply Log Transformation (log(1 + x) to handle zeros)
log_transformed_df = np.log1p(df)  # log(1 + x)
print(log_transformed_df)
