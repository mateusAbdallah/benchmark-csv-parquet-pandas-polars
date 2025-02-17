
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

