import streamlit as st
import pandas as pd
import numpy as np
import graphviz

# 1. Write and Magic
st.title("1. Write and Magic")

df = pd.DataFrame({
  'Bulan': ['1. Januari', '2. Februari', '3. Maret', '4. April', '5. Mei'],
  'Komputer': np.random.randint(100, 1000, 5),
  'Laptop': np.random.randint(100, 1000, 5),
  'Speaker': np.random.randint(100, 1000, 5)
})

st.subheader("print with st.write:")
st.write(df.set_index('Bulan'))

st.write('#')
st.subheader("print with magic:")
df

# 2. Text Elements with st.code
st.write("#")
st.title("2. Text Elements")

st.markdown(":green[$c= \sqrt{a^2+b^2}$]")
code = '''
# pythagoras function
def pythagoras(a,b):
    return sqrt(a**2 + b**2);
    
result = pythagoras(3,4)
print(result)
'''
st.code(code, language='python')
st.write("result = 5")

# 3. Data Display Elements with st.checkbox and dataframe
st.write("#")
st.title("3. Data Display Elements")

df = pd.DataFrame({
  'Bulan': ['1. Januari', '2. Februari', '3. Maret', '4. April', '5. Mei'],
  'Pendapatan': [20000, 35000, 47000, 26000, 59000]
}, index=[1,2,3,4,5])

st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df.style.highlight_max(axis=0), use_container_width=st.session_state.use_container_width)

# 4. Chart Elements with st.graphviz_chart
st.write("#")
st.title("4. Chart Elements")

graph = graphviz.Digraph()
graph.edge('Mulai', 'Masukan Bilangan Prima')
graph.edge('Masukan Bilangan Prima', 'Bilangan di Modulus')
graph.edge('Bilangan di Modulus', 'Apakah modulus = 0')
graph.edge('Apakah modulus = 0', 'Genap')
graph.edge('Apakah modulus = 0', 'Ganjil')
graph.edge('Genap', 'Selesai')
graph.edge('Ganjil', 'Selesai')

st.graphviz_chart(graph)

#  5. Input Widgets with st.radio
st.write("#")
st.title("5. Input Widgets")

genre = st.radio(
    "2 x 2 x 3 x 0 + 1 X 2",
    ('2', '12', '6'))

if genre == '2':
    st.write('You Right')
else:
    st.write("You Wrong")

# 6. Media Elements with st.video
st.write("#")
st.title("6. Media Elements")
st.video("https://www.youtube.com/watch?v=0PBpAEGuNHM")

# 7. Layouts and Containers with st.column
st.write("#")
st.title("7. Layouts and Containers")

col1, col2, col3 = st.columns(3)

with col1:
   st.image("https://cdn.thenewstack.io/media/2021/11/28de6660-screen-shot-2021-11-29-at-6.46.11-am.png")

with col2:
   st.image("https://mms.businesswire.com/media/20200616005364/en/798639/23/Streamlit_Logo_%281%29.jpg")

# 8. Status Elements with st.progress
st.write("#")
st.title("8. Status Elements")

if st.button('Click Button'):
    st.success('This is a success message!', icon="✅")
else:
    st.write('Please Click The Button!')

# 9. Utilities with st.echo
st.write("#")
st.title("9. Utilities with st.stop")

with st.echo():
    st.write('Hello World')

# 10. Control Flow with st.stop
st.write("#")
st.title("10. Control Flow")

name = st.text_input('Name')
if not name:
  st.warning('Please input name.')
  st.stop()
st.success('Thank you for inputting a name.')