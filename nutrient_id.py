#FF_NDB,SR_NDB,food_category_id,FF Food description,SR Food description,Nutrient_id,rank,FF_Component,SR_Component,unit_name,SR Mean per 100g,SR Min,SR Max, Std_Error,SR Num_Data_pts,FF Mean per 100g,FF Min,FF Max,FF Median,FF data_points,FF Publication Date
import numpy as np
import pandas as pd

ffsr = pd.read_csv('FF_SR_ data.csv')
dancsv = pd.read_csv('food_stdev_diff.csv')

comp_std = ffsr.groupby('FF_Component')['FF Mean per 100g'].std() 
ffsr['avg_stdev_diff']=comp_std
ffsr['FF_std'] = ffsr['FF Mean per 100g']/ffsr['FF_Component'].map(comp_std)
ffsr['SR_std'] = ffsr['SR Mean per 100g']/ffsr['FF_Component'].map(comp_std)
ffsr['component_diff'] = abs(ffsr['FF_std']-ffsr['SR_std'])
ffsr = ffsr.merge(dancsv, how='left', validate='many_to_one').fillna(0)
nutrient = ffsr
ffsr.to_csv('std_nutrient_id.csv')
