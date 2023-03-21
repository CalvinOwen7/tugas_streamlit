import streamlit as st
import pandas as pd

# Linechart dengan dataframe yang dibuat manual
st.header("Pendapatan Per Bulan")

df = pd.DataFrame({
  'Bulan': ['1. Januari', '2. Februari', '3. Maret', '4. April', '5. Mei'],
  'Pendapatan': [20000, 35000, 27000, 36000, 49000]
}, index=[1,2,3,4,5])

st.write('Tabel:')
st.dataframe(df, width=400)
st.markdown('#')

st.write('Linechart:')
st.line_chart(df, x='Bulan')
