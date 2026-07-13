from sklearn.datasets import load_iris
import pandas as pd m

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["flower"] = iris.target

print(df)
