import streamlit as st
from streamlit_local_storage import LocalStorage

localStorage = LocalStorage()
st.write(localStorage.getAll())
#localStorage.deleteAll()

st.info('Encontrado')
st.write(localStorage.getAll())

st.info('enchendo...')
localStorage.setItem("dados", [[12, 3, 4, 5, 6, 7], [2, 4, 5],
                               [0], [2222]])
st.write(localStorage.getAll())

import pypickle
#Arquivo pickle
filepath = 'test.pkl'

# Some data
data = [1,2,3,4,5]

# Save
status = pypickle.save(filepath, data)

# Load file
data = pypickle.load(filepath)
st.write(data)

value = st.slider(label="Select a range of values", 
                  min_value=-100, 
                  max_value=100, 
                  value=0, 
                  label_visibility="hidden", 
                  key='slider')

with open('teste.css') as f:
    css = f.read()

html = """
<hmtl>
  <body>
    <p class="center">This paragraph refers to two classes.</p>
    <p id="para1">Hello World!</p>
    <h1>My First CSS Example</h1>
    <p>Sempre ganharemos a batalha.</p>
    <h3>My First CSS Example - H3</h3>
    <h4>My First CSS Example - H$</h4>
    <h5>My First CSS Example - H5</h5>
  </body>
</html>
"""
st.markdown(html, unsafe_allow_html=True)
#Maneiras de inserir CSS externo no streamlit.
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#st.markdown("<link rel='stylesheet'" "href={css}>", unsafe_allow_html=True)
