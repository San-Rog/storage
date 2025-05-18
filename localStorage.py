import streamlit as st
from streamlit_local_storage import LocalStorage

localS = LocalStorage()
#st.error('deletando...')
st.info('Encontrado')
st.write(localS.getAll())

st.info('enchendo...')
localS.setItem('mama', 10)
localS.setItem('lema', 20)

