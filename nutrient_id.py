#FF_NDB,SR_NDB,food_category_id,FF Food description,SR Food description,Nutrient_id,rank,FF_Component,SR_Component,unit_name,SR Mean per 100g,SR Min,SR Max, Std_Error,SR Num_Data_pts,FF Mean per 100g,FF Min,FF Max,FF Median,FF data_points,FF Publication Date
import numpy
import pandas as pd

ffsr = pd.read_csv('FF_SR_ data.csv')
ff_comp = ffsr.groupby('FF_Component') #this is working lol 

std = ff_comp['FF Mean per 100g']
print(std.get_group('Water'))
#ff_comp['std'] = std
#std_ff = ff_comp['std'].std()
#print(std_ff)
# ff_std = ffsr[ffsr[]]