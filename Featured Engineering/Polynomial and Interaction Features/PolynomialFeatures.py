from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# Sample data
data = {'X1': [1, 2, 3, 4], 'X2': [2, 3, 4, 5]}
df = pd.DataFrame(data)

# Initialize PolynomialFeatures with degree 2
poly = PolynomialFeatures(degree=2)

# Generate polynomial features
poly_features = poly.fit_transform(df)

# Convert to DataFrame for better readability
poly_df = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(df.columns))

print(poly_df)
