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


# for ind in stdevs_df.index:
#     if stdevs_df['SR Food description'][ind] == 'Hummus, commercial':
#         print(stdevs_df['Nutrient_id'][ind],stdevs_df['stdev_difference'][ind])


# Find average STDEV error over each food group.
mean0 = stdevs_df.groupby('SR Food description',as_index=False)[['stdev_difference']].mean()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DO NOT RUN THESE LINES AGAIN!!!!!!! THE FILE ALREADY EXISTS!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print(mean0)
# mean_tup_list = []
# for ind in mean0.index:
#     mean_tup_list.append((mean0['SR Food description'][ind],mean0['stdev_difference'][ind]))

# with open('food_stdev_diff.csv', 'w') as file:
#     file.write('name,avg_stdev_diff\n')
#     for tupl in mean_tup_list:
#         file.write(f'"{tupl[0]}",{tupl[1]}\n')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


