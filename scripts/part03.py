# %%
import part02_polars
import part02
import part01

import matplotlib.pyplot as plt
import streamlit as st

# %%

df = part02.df

# %%

st.title("Stock Price Prediction Dashboard")

# %%

companies = df["name"].unique().tolist()
selected_company = st.selectbox("Select a Company", companies)
df_company = df.filter(df['name'] == selected_company)


# %% 

# Plot Predictions
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(part02_polars.test["date"], part02_polars.y_test, label='Actual Close Price', color='blue')
ax.plot(part02_polars.test["date"], part02_polars.lr_pred, label='Linear Regression Prediction', color='red', linestyle='dashed')
ax.plot(part02_polars.test["date"], part02_polars.rf_pred, label='Random Forest Prediction', color='green', linestyle='dotted')
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_title(f'Price Prediction for {selected_company}')
ax.legend()
st.pyplot(fig)
# %%

# Display metrics

st.write(f'**Linear Regression RMSE:** {part02.lr_rmse:.2f}')
st.write(f'**Random Forest RMSE:** {part02.rf_rmse:.2f}')

# %%

st.bar_chart(x=range(10), y=[part01.writing_1x_parquet, part01.writing_10x_parquet, part01.writing_100x_parquet])
st.bar_chart(x=range(10), y=[part01.writing_10x_csv, part01.writing_100x_csv])

# %%

st.bar_chart(x=range(10), y=[part01.reading_1x_parquet, part01.reading_10x_parquet, part01.reading_100x_parquet])
st.bar_chart(x=range(10), y=[part01.reading_1x_csv, part01.reading_10x_csv, part01.reading_100x_csv])

