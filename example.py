import pandas as pd

df = pd.read_csv('exampledf.csv')
stdevs = df.groupby('name',as_index=False)[['mean2']].std()
stdevs = stdevs.rename(columns={"mean2": "stdev"})


df = df.merge(stdevs,on='name')
print(df)
stdev_list = []
for ind in df.index:
    stdev_list.append(abs((df['mean2'][ind]-df['mean1'][ind])/df['stdev'][ind]))
df['stdev_difference'] = stdev_list
print(df)