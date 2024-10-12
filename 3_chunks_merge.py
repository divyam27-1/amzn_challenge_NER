import os
import pandas as pd 

chunk_files = [f"chunk_{i}.csv" for i in range(1, 31)]

dataframes = []
for file in chunk_files:
    if os.path.exists(file):
        df = pd.read_csv(file)
        dataframes.append(df)
    else:
        print(f"Warning: {file} does not exist and will be skipped.")

merged_df = pd.concat(dataframes, ignore_index=True)

merged_df.to_csv("merged_chunks.csv", index=False)

print("Merging complete.")
