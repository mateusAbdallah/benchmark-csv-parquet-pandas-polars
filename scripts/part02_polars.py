# %%
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# %%
# Load dataset using Polars
df = pl.read_csv("../data/all_stocks_5yr.csv")
# %%
# Convert date to datetime format
df = df.with_columns(pl.col("date").str.to_datetime())
# %%
# Sort data by stock name and date
df = df.sort(["name", "date"])
# %%
# Create Previous Day Closing Price
df = df.with_columns(pl.col("close").shift(1).alias("prev_close"))
df = df.drop_nulls()
# %%
# Train-test split (80-20)
train, test = train_test_split(df.to_pandas(), test_size=0.2, shuffle=False)
# %%
# Features and Target
X_train, X_test = train[["prev_close"]], test[["prev_close"]]
y_train, y_test = train["close"], test["close"]
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
