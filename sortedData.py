import pandas as pd
import fetchData

df = pd.read_csv(fetchData.processed_file_path)
print(df.columns)

df_sorted = df.sort_values(by='Region')
print(df_sorted)

sorted_file_path = fetchData.processed_file_path.replace('processed_', 'sorted_')
df_sorted.to_csv(sorted_file_path, index=False)

print(f"Sorted file saved as {sorted_file_path}")