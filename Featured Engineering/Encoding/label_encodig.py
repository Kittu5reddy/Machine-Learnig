from sklearn.preprocessing import LabelEncoder
import pandas as pd


data = {'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']}
df = pd.DataFrame(data)


label_encoder = LabelEncoder()


df['Size_encoded'] = label_encoder.fit_transform(df['Size'])

print(df)
