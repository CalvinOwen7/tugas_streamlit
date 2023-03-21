import streamlit as st
import pandas as pd
import numpy as np

# Checkbox Widget
np.random.seed(200)
df = pd.DataFrame({
  'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
  'Komputer': np.random.randint(100, 1000, 5),
  'Laptop': np.random.randint(100, 1000, 5),
  'Speaker': np.random.randint(100, 1000, 5)
  }, index=[1,2,3,4,5])

st.subheader('Table:')
st.dataframe(df)

show = st.checkbox('Show Linechart')
if show:
  st.markdown('#')
  st.subheader('linechart:')
  st.line_chart(df.set_index('Bulan'))