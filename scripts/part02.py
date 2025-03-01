# %%
import pandas as pd

# %%

df = pd.read_csv('../data/all_stocks_5yr.csv')

# %%
# Simple Moving Average
df['SMA_20'] = df.groupby('name')['close'].transform(lambda x: x.rolling(window=20).mean())

# %%
# Exponential Moving Average
df['EMA_20'] = df.groupby('name')['close'].transform(lambda x: x.ewm(span=20, adjust=False).mean())

# %%
# Relative Strength Index

df['price_change'] = df.groupby('name')['close'].diff()
df['gain'] = df['price_change'].apply(lambda x: x if x > 0 else 0)
df['loss'] = df['price_change'].apply(lambda x: -x if x < 0 else 0)

df['avg_gain'] = df.groupby('name')['gain'].transform(lambda x: x.rolling(window=20).mean())
df['avg_loss'] = df.groupby('name')['loss'].transform(lambda x: x.rolling(window=20).mean())


df['rs'] = df['avg_gain'] / df['avg_loss']
df['rsi'] = 100 - (100 / (1 + df['rs']))

# %%
# On-Balance Volume
df['obv'] = df.groupby('name').apply(lambda x: x['volume'] * (1 if x['close'].diff().iloc[-1] > 0 else -1)).reset_index(level=0, drop=True)

df['obv'] = df.groupby('name')['obv'].cumsum()

# %%

df = df.rename(columns={'SMA_20':'sma_20', 'EMA_20':'ema_20'})
