import pandas as pd


df = pd.read_csv('mydata.csv')
df = df[['SR_NDB','SR Food description','Nutrient_id','SR Mean per 100g','FF Mean per 100g']] # Fileter data frame to what we need.
stdevs0 = df.groupby('Nutrient_id',as_index=False)[['FF Mean per 100g']].std() # New data frame with Stdevs of FF mean
stdevs0 = stdevs0.rename(columns={"FF Mean per 100g": "stdev"}) # Rename FF mean column of new df to stdev.


stdevs_df = df.merge(stdevs0,on='Nutrient_id') # Merge; new df has both means and stdev
stdevs_df = stdevs_df.sort_values('SR Food description') # Sort by food type
stdevs_df = stdevs_df.reset_index() # reset index



stdev_list = []
for ind in stdevs_df.index: # calculates stdev difference for every row of df.
    stdev_list.append(abs((stdevs_df['FF Mean per 100g'][ind]-stdevs_df['SR Mean per 100g'][ind])/stdevs_df['stdev'][ind]))
stdevs_df['stdev_difference'] = stdev_list # Adds stdev differences to df.
print(stdevs_df) # 'stdevs_df' has Food description, both means, stdevs, and stdev differences.
