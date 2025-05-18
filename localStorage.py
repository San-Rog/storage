import streamlit as st
from streamlit_local_storage import LocalStorage

localStorage = LocalStorage()
st.write(localStorage.getAll())
localStorage.deleteAll()

st.info('Encontrado')
st.write(localStorage.getAll())

st.info('enchendo...')
localStorage.setItem("nome", "João");
try:
  localStorage.setItem("idade", "30");
  localStorage.setItem("cidade", "São Paulo");
except:
  st.write('não entraram', "idade", "30")
st.write(localStorage.getAll())

