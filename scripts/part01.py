
# %%
import pandas as pd

# %%

df = pd.read_csv('../data/all_stocks_5yr.csv')
df.head()

# %%

df.info(memory_usage='deep')
 # %%

df.iloc[0:]

# %%

# Scaling dataset 10x

df_scaled_10x = pd.concat([df] * 10, ignore_index=True)
df_scaled_10x.info(memory_usage='deep')

# %%

# Scaling dataset 100x

df_scaled_100x = pd.concat([df] * 100, ignore_index=True)
df_scaled_100x.info(memory_usage='deep')

# %%
# Saving csv dataframe scaled 10x

df_scaled_10x.to_csv('../data/df_10x.csv')

# %%
# Saving csv dataframe scaled 100x

df_scaled_100x.to_csv('../data/df_100x.csv')

# %%

# Saving parquet dataframe scaled 1x

#f.to_parquet('../data/df_1x.parquet')

# %%

# Saving parquet dataframe scaled 10x

df_scaled_10x.to_parquet('../data/df_10x.parquet')

# %%

# Saving parquet dataframe scaled 100x

df_scaled_100x.to_parquet('../data/df_100x.parquet')

# %%
df_1x = pd.read_parquet('../data/df_1x.parquet')
df_1x.info(memory_usage='deep')

# %%
df_10x = pd.read_parquet('../data/df_10x.parquet')
df_10x.info(memory_usage='deep')

