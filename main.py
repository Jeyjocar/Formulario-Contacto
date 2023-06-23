import streamlit as st
import requests 
from streamlit_lottie import st_lottie  

# darle nombre a la pagina
st.set_page_config(page_title='Desarrollo con Streamlit?',layout='wide',page_icon=':💻:')

#funcion para traer la respuesta desde la url
def cargarIcons(url):
 respuesta = requests.get(url)
 if respuesta.status_code != 200:
     return None
 return respuesta.json()

def estilos(archivo):
    with open(archivo) as file:
        st.markdown(f'<style>{file.read()}</style>',unsafe_allow_html=True)
        
estilos('css/style.css')


#cargar respuesta desde la url 'icono' 
icons = cargarIcons('https://assets9.lottiefiles.com/packages/lf20_3vbOcw.json')
with st.container():
    # crear un titulo para el contenedor principal de nuestra aplicacion
    st.write('Jeyfrey Calero_inc.')
    #creamos 2 variables para columnas y filas
    colLeft,colrigth = st.columns(2)
    with colLeft:
        st.header('Hola :wave:, ¿Necesitas un Programador?...')
        st.subheader('Lista de datos')
        st.write('Vamos a probar CSS y HTML')
    with colrigth:
        st_lottie(icons,height=300,key='hello')
        
#SIGUIENTE CONTAINER
with st.container():
    # crear un titulo para el contenedor principal de nuestra aplicacion
    st.write('Soy desarrollador web en Backend con Python, Javascript, CSS y HTML')
    #creamos 2 variables para columnas y filas
    colLeft,colrigth = st.columns(2)
    with colLeft:
        st.header('Empecé mi formación en desarrollo WEB desde el 2022 de forma autonoma y autodidacta')
        st.write('''
            Desarrollo WEB,
            Maquetación HTML5,
            CSS3''')
        st.write('Dime en que puedo ayudarte...')
    with colrigth:
        st_lottie(icons,height=300,key='Chao, Bye, Ciao, A biento')
        
        with st.container():
            st.write('---')
            st.header('Contactanos')
            st.write('##')
            Contacto = '''
            <form action="https://formsubmit.co/omar.toledus@gmail.com" method="POST">
            <input type='hidden'name='_captcha' value='false'>
            <input type="text", placeholder='nombre', name="name" required>
            <input type="email", placeholder='tu correo' name="email" required>
            <textarea name='message' placeholder='dejanos un mensaje', required></textarea>
            <button type="submit">Enviar</button>
            </form>'''
            colLeft,colrigth = st.columns(2)
            with colLeft:
                st.markdown(Contacto,unsafe_allow_html=True)
            with colrigth:
                st.empty()
            
            
            
        
        
 