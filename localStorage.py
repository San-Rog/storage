import streamlit as st
from streamlit_local_storage import LocalStorage

localStorage = LocalStorage()
localStorage.deleteAll()

st.info('Encontrado')
st.write(localS.getAll())

st.info('enchendo...')
localStorage.setItem("nome", "João");
localStorage.setItem("idade", "30");
localStorage.setItem("cidade", "São Paulo");
st.write(localS.getAll())

