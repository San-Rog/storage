import streamlit as st
from streamlit_local_storage import LocalStorage

localS = LocalStorage()
#st.error('deletando...')
st.info('Encontrado')
st.write(localS.getAll())

st.info('enchendo...')
#Gravar o para chave-valor em localstorage
for categ, pairs in {'dados': ['Zebra', 'tratmento', 'tubo', 'martelo'], 
                    'membros': [12, 4, 6]}.items():    
    itemKey = categ
    itemValue = pairs
    st.write(itemKey)
    st.write(itemValue)
    #st.write(localS.getAll())
    try:
      localS.setItem(itemKey, itemValue)
    except:
      pass
st.success("Gravação exitosa")

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


