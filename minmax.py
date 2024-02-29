#FF_NDB,SR_NDB,food_category_id,FF Food description,SR Food description,Nutrient_id,rank,FF_Component,SR_Component,unit_name,SR Mean per 100g,SR Min,SR Max, Std_Error,SR Num_Data_pts,FF Mean per 100g,FF Min,FF Max,FF Median,FF data_points,FF Publication Date
import pandas as pd
import plotly.express as px


df = pd.read_csv('mydata.csv')
df = df[['SR_NDB','SR Food description','Nutrient_id','SR_Component','SR Mean per 100g','FF Mean per 100g']] # Fileter data frame to what we need.
stdevs0 = df.groupby('Nutrient_id',as_index=False)[['FF Mean per 100g']].std() # New data frame with Stdevs of FF mean
stdevs0 = stdevs0.rename(columns={"FF Mean per 100g": "stdev"}) # Rename FF mean column of new df to stdev.


stdevs_df = df.merge(stdevs0,on='Nutrient_id') # Merge; new df has both means and stdev
stdevs_df = stdevs_df.sort_values('SR Food description') # Sort by food type
stdevs_df = stdevs_df.reset_index() # reset index



stdev_list = []
for ind in stdevs_df.index: # calculates stdev difference for every row of df.
    stdev_list.append(abs((stdevs_df['FF Mean per 100g'][ind]-stdevs_df['SR Mean per 100g'][ind])/stdevs_df['stdev'][ind]))
stdevs_df['stdev_difference'] = stdev_list # Adds stdev differences to df.
# print(stdevs_df) # 'stdevs_df' has Food description, both means, stdevs, and stdev differences.
stdevs_df = stdevs_df.drop(['index'],axis=1)

nutrient_df = stdevs_df.groupby('SR_Component',as_index=False)[['stdev_difference']].mean() # New data frame with Stdevs of FF mean
nutrient_df = nutrient_df.rename(columns={"stdev_difference": "mean_stdev_difference"})
sorted =nutrient_df.sort_values('mean_stdev_difference')

sorted.to_csv('max_nutrient_id.csv')


##################################################################################################
max_nut = pd.read_csv('max_nutrient_id.csv')
print(max_nut)
fig = px.bar(max_nut, x="SR_Component", y="mean_stdev_difference", color="SR_Component", barmode="group")
fig.show()
#################################################################################################