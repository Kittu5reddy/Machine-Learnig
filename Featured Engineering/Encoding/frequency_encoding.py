import pandas as pd


data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Red']}
df = pd.DataFrame(data)

frequency = df['Color'].value_counts()  
df['Color_encoded'] = df['Color'].map(frequency)  

print(df)
