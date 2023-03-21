import streamlit as st
import pandas as pd
import numpy as np

# Layout Column
st.header('Data Pendapatan')

np.random.seed(200)
df = pd.DataFrame({
  'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
  'Komputer': np.random.randint(100, 1000, 5),
  'Laptop': np.random.randint(100, 1000, 5),
  'Speaker': np.random.randint(100, 1000, 5)
  }, index=[1,2,3,4,5])

col1, col2 = st.columns(2)
with col1:
  st.subheader('Tabel :')
  st.dataframe(df)

with col2:
  st.subheader('Linechart:')
  st.line_chart(df.set_index('Bulan'))