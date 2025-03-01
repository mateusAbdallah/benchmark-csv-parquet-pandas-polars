# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

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
# Rename columns
df = df.rename(columns={'SMA_20':'sma_20', 'EMA_20':'ema_20'})
# Drop null values
df = df.dropna()

# %%

features = df.drop(columns=['date', 'close', 'name']) 
target = df['close']

# %%

X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=10, test_size=0.2)

# %%

# Linear Regression

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# %%

# Random Forest Model

rf_model = RandomForestRegressor(n_estimators=10, random_state=10)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
