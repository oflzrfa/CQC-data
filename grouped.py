import pandas as pd
import fetchData

df = pd.read_csv(fetchData.processed_file_path)
print(df.columns)

df.rename(columns={
    'Specialisms/services': 'Specialisms', 
    'Service types': 'ServiceTypes'
}, inplace=True)

required_columns = ['Region', 'Specialisms', 'ServiceTypes']
df_filtered = df[required_columns].dropna()

grouped_df = df_filtered.groupby(['Region', 'Specialisms', 'ServiceTypes']).size().reset_index(name='Count')

sorted_df = grouped_df.sort_values(by=['Region', 'Specialisms', 'ServiceTypes'])
print(sorted_df)

grouped_sorted_file_path = fetchData.processed_file_path.replace('processed_', 'grouped_sorted_')
sorted_df.to_csv(grouped_sorted_file_path, index=False)

print(f"Sorted and grouped file saved as {grouped_sorted_file_path}")
