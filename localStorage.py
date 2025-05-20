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

