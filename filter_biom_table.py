import biom
from biom import load_table
import pandas as pd


table = load_table('data/skin_1975.biom').to_dataframe(dense=True).T.astype(int)
age_metadata = pd.read_csv('data/skin_1975_map.txt', sep='\t', index_col=0, dtype={'qiita_host_age': float})
age_metadata = age_metadata.drop_duplicates(subset='host_subject_id')
table = table.loc[age_metadata.index].T

# Convert DataFrame to BIOM table
filtered_table = biom.Table(table.values, observation_ids=table.index.tolist(), sample_ids=table.columns.tolist())

# Save BIOM table to file
with biom.util.biom_open('filtered_table.biom', 'w') as f:
    table.to_hdf5(f, "example")