import pandas as pd
import plotly.express as px
food_data = pd.read_csv('FF_SR_ data.csv')

hummus = food_data[food_data['FF_NDB'] == 16158]
FF_sort = hummus.sort_values('FF Mean per 100g', ascending=False)
SR_sort = hummus.sort_values('SR Mean per 100g', ascending=False)

ratio = hummus['FF Mean per 100g']/hummus['SR Mean per 100g']
print(ratio)

#fig = px.scatter(data_frame=food_data, x='FF Mean per 100g', y='SR Mean per 100g', hover_data='FF Food description', trendline='ols') #put into a scatter plot
#fig.show()