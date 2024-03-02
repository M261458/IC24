import pandas as pd
import re
import plotly.graph_objects as go

food_data = pd.read_csv('jillpie.csv')
labels =[]
values = []
for i,row in food_data.iterrows():
    labels.append(food_data['Food'][i])
    values.append(food_data['count'][i])
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()


# csv = open('nutrient_stdev_diff.csv')
# food_name = r'^"[A-Z][a-z]* '
# food_name2 = r'^"[A-Z][a-z]*,'
# totmatches = []
# for line in csv:
#      matches2 = re.search(food_name2, line)
#      matches = re.search(food_name, line)
#      totmatches.append(matches2)
#      totmatches.append(matches)

# import plotly.express as px
# data = 'jillpie.csv'
# df = px.data.tips()
# fig = px.pie(df, values = 'count',names = 'Food')
# fig.show()


# topfoods = pd.read_csv('nutrient_stdev_diff.csv')
# description = topfoods['SR Food description']
# foodsonce = []
# for i,row in topfoods.iterrows():
#     print(row)
#     if description in foodsonce:
#         continue
#     elif description not in foodsonce:
#         foodsonce.append(description)
