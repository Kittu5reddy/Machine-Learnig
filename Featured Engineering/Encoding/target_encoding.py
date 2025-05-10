import pandas as pd


data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Green'],
        'Target': [1, 0, 1, 0, 1, 0]}
df = pd.DataFrame(data)

target_encoding = df.groupby('Color')['Target'].mean()


df['Color_encoded'] = df['Color'].map(target_encoding)

print(df)
