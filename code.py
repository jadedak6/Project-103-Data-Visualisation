from google.colab import files
data_to_load = files.upload()

import pandas as pd

import plotly.express as px

df = pd.read_csv("data1.csv")
fig = px.bar(df, x='City', y='People who read')
fig.show()
