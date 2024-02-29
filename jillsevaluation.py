#chickpeas
#kale
#mitake

#3,6,10,16

import pandas as pd
import plotly.express as px

food_stdev = pd.read_csv('food_stdev_diff.csv')
avg_stdev = food_stdev.sort_values('avg_stdev_diff', ascending = False)
above3 = avg_stdev[ avg_stdev['avg_stdev_diff'] > 0.3 ]

top10 = pd.read_csv('jillcsv.csv')
namelist = []
valuelist =[]
for i,row in top10.iterrows():
    namelist.append(top10['Name of Food'][i])
    valuelist.append(top10['Average Standard Deviation Difference'][i])
print(namelist)
print(valuelist)
fig = px.bar(top10, x = 'Name of Food', y = 'Average Standard Deviation Difference', color = 'Name of Food')
fig.show()