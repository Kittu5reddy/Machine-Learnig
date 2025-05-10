import pandas as pd

# Sample data
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# Apply One-Hot Encoding
one_hot_encoded_df = pd.get_dummies(df, columns=['Color'], prefix='Color')

print(one_hot_encoded_df)
