import streamlit as st
from streamlit_local_storage import LocalStorage

localS = LocalStorage()
#st.error('deletando...')
st.info('Encontrado')
st.write(localS.getAll())

st.info('enchendo...')

def supply(itemKey, itemValue):
    itemKey = categ
    itemValue = pairs
    st.write(itemKey)
    st.write(itemValue)
    localS.setItem(itemKey, itemValue)
st.success("Gravação exitosa")

itemKey = 'dados' 
itemValue = ['Zebra', 'tratmento', 'tubo', 'martelo']
supply(itemKey, itemValue)
itemKey = 'zebra' 
itemValue = ['carrro', 0, 12, 14]
supply(itemKey, itemValue)
st.write(localS.getAll())

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


