# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# %%

df = pd.read_csv('../data/all_stocks_5yr.csv')
df
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
# %%
df['prev_close'] = df.groupby('name')['close'].shift(1)
df = df.dropna()  # Drop NaN values from shifting


# %% 

# Train-test split (80-20)
train, test = train_test_split(df, test_size=0.2, shuffle=False)

# Features and Target
X_train, X_test = train[['prev_close']], test[['prev_close']]
y_train, y_test = train['close'], test['close']
# %%

# Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
# %%

# Random Forest Model
rf_model = RandomForestRegressor(n_estimators=50, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# %%

# Evaluate Models

lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
