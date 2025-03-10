
# %%
import pandas as pd
import timeit   
import streamlit as st

# %%
# Reading and checking reading time
start_time = timeit.default_timer()
df = pd.read_csv('../data/all_stocks_5yr.csv')
df.head()
reading_1x_csv = timeit.default_timer() - start_time


# %%

# Scaling dataset 10x

df_scaled_10x = pd.concat([df] * 10, ignore_index=True)
df_scaled_10x.info(memory_usage='deep')

# %%

# Scaling dataset 100x

df_scaled_100x = pd.concat([df] * 100, ignore_index=True)
df_scaled_100x.info(memory_usage='deep')

# %%

# Saving csv dataframe scaled 10x / checking writing time
start_time = timeit.default_timer()
df_scaled_10x.to_csv('../data/df_10x.csv')
writing_10x_csv = timeit.default_timer() - start_time

# %%

# Saving csv dataframe scaled 100x / checking writing time
start_time = timeit.default_timer()
df_scaled_100x.to_csv('../data/df_100x.csv')
writing_100x_csv = timeit.default_timer() - start_time

# %%

# Checking reading time
start_time = timeit.default_timer() 
read_10x = pd.read_csv('../data/df_10x.csv')
reading_10x_csv = timeit.default_timer() - start_time

# %%

# Checking reading csv time
start_time = timeit.default_timer() 
read_100x = pd.read_csv('..data/df_100x.csv')
reading_100x_csv = timeit.default_timer() - start_time

# %%

# Saving parquet dataframe scaled 1x / checking writing time
start_time = timeit.default_timer()
df.to_parquet('../data/df_1x.parquet')
writing_1x_parquet = timeit.default_timer() - start_time

# %%

# Saving parquet dataframe scaled 10x / checking writing time
start_time = timeit.default_timer()
df_scaled_10x.to_parquet('../data/df_10x.parquet')
writing_10x_parquet = timeit.default_timer() - start_time
# %%

# Saving parquet dataframe scaled 100x / checking writing time
start_time = timeit.default_timer()
df_scaled_100x.to_parquet('../data/df_100x.parquet')
writing_100x_parquet = timeit.default_timer() - start_time
# %%

# Checking reading time
start_time = timeit.default_timer()
df_1x = pd.read_parquet('../data/df_1x.parquet')
reading_1x_parquet = timeit.default_timer() - start_time
# %%

# Checking reading time
start_time = timeit.default_timer()
df_10x = pd.read_parquet('../data/df_10x.parquet')
reading_10x_parquet = timeit.default_timer() - start_time
# %%

# Checking reading time
start_time = timeit.default_timer()
df_100x = pd.read_parquet('../data/df_100x.parquet')
reading_100x_parquet = timeit.default_timer() - start_time

