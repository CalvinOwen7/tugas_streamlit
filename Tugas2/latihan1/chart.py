import streamlit as st
import pandas as pd
import numpy as np

# Bar-chart
np.random.seed(200)
df = pd.DataFrame({
  'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
  'Komputer': np.random.randint(100, 1000, 5),
  'Laptop': np.random.randint(100, 1000, 5),
  'Speaker': np.random.randint(100, 1000, 5)
  })

st.write('Show bar-chart:')
st.bar_chart(df.set_index('Bulan'))