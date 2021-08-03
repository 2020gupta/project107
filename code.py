import pandas as pd
import csv
import plotly.express as px
df=pd.read_csv("data.csv")
mean=df.groupby(["studentid","level"],as_index=False)["attempt"].mean()
graph=px.scatter(mean,x="studentid",y="level",size="attempt",color="attempt")
graph.show()