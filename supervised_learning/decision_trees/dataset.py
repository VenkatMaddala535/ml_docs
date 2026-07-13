import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data,columns=iris.feature_names)

df["flower"] = iris.target

print(df.head())

