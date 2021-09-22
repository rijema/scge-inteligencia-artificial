import plotly.express as px
import pandas as pd
data = pd.read_csv(r'C:\\Users\\Felipe P. Maciel\\Documents\\ECOMP\\Inteligência Artificial\\preProcessado2.csv')
fig = px.scatter_3d(data, x='x', y='y', z='z')
fig.show()