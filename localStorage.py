import streamlit as st
from streamlit_local_storage import LocalStorage
import pyautogui

localS = LocalStorage()
localS.deleteAll()

#Gravar o para chave-valor em localstorage
for categ, pairs in {'dados': ['Zebra', 'tratmento', 'tubo', 'martelo']}.items():    
    itemKey = categ
    itemValue = pairs
    st.write(itemKey)
    st.write(itemValue)
    st.write(localS.getAll())
    localS.setItem(itemKey, itemValue)
st.success("Gravação exitosa")

#Ler a chave camera.
#itemKey = "camera"
#storageItem = localS.getItem(itemKey)
#st.info(storageItem)

#Ler todos os pares chae-valor em LocalStorage
#allItens = localS.getAll()
#st.write(allItens)

#Apagar tudo em localStorage
#localS.deleteAll()

#allItens = localS.getAll()
#st.write(allItens)

if st.button('fechar'):
    pyautogui.hotkey('ctrl+w')

