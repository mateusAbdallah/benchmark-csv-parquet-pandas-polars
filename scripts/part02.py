# %%
import pandas as pd

# %%

df = pd.read_csv('../data/all_stocks_5yr.csv')

# %%

df_filter_ko = df['name'] == "KO"
df[df_filter_ko]

# %%

ko_14 = df[df_filter_ko]
ko_14

 # %%
#Simple Moving Average
ko_14['SMA'] = ko_14['close'].mean()

# appl_max = appl_14['close'].max()
# appl_min = appl_14['close'].min()
