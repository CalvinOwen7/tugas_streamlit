import streamlit as st
import pandas as pd
import numpy as np

# Bar-chart
np.random.seed(200)
df = pd.DataFrame({
  'Bulan': ['1. Januari', '2. Februari', '3. Maret', '4. April', '5. Mei'],
  'Komputer': np.random.randint(100, 1000, 5),
  'Laptop': np.random.randint(100, 1000, 5),
  'Speaker': np.random.randint(100, 1000, 5)
  })

st.write('Show bar-chart:')
st.bar_chart(df.set_index('Bulan'))