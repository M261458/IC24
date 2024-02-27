import pandas as pd

df = pd.read_csv('exampledf.csv')
stdevs = df.groupby('name',as_index=False)[['mean2']].std()
stdevs = stdevs.rename(columns={"mean2": "stdev"})


df = df.merge(stdevs,on='name')



stdev_list = []
for ind in df.index:
    stdev_list.append(abs((df['mean2'][ind]-df['mean1'][ind])/df['stdev'][ind]))
df['stdev_difference'] = stdev_list


# Find average STDEV error over each food group.
mean0 = df.groupby('name',as_index=False)[['stdev_difference']].mean()
mean_tup_list = []
for ind in mean0.index:
    mean_tup_list.append((mean0['name'][ind],mean0['stdev_difference'][ind]))

with open('mean_diff.csv', 'w') as file:
    file.write('name,avg_stdev_diff\n')
    for tupl in mean_tup_list:
        file.write(f'{tupl[0]},{tupl[1]}\n')
