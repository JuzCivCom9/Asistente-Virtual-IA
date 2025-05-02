
import streamlit as st

st.set_page_config(page_title="Asistente Virtual IA - Juzgado N° 9", layout="centered")

st.title("Asistente Virtual IA")
st.subheader("Juzgado Civil y Comercial N° 9 - Departamento Judicial La Matanza")
st.markdown("""
**Bienvenido/a al Asistente Virtual IA del Juzgado Civil y Comercial N° 9 – Departamento Judicial La Matanza.**  
A través de este asistente podrá evacuar las consultas más frecuentes.  
Seleccione una opción o escriba su duda.  
**Este servicio no implica ningún tipo de asesoramiento jurídico ni constituye una vía de contacto procesal.**
""")

opciones = [
    "Requisitos para inscribir declaratoria de herederos",
    "Visualización de expediente como e-book",
    "Uso de TICs en audiencias (BLSG)",
    "Redes sociales del juzgado",
    "Encuestas de satisfacción",
    "Contacto con SADyP (Zoom)"
]

consulta = st.selectbox("Seleccione un tema:", opciones)

if consulta == opciones[0]:
    st.markdown("""
**Inscripción de declaratoria de herederos:**  
[Ver instructivo (OneDrive)](https://scbagovar-my.sharepoint.com/:b:/g/personal/rcsdellaporta_scba_gov_ar/EajRyx2zlyJPiYR8jb1h2sABvpMp61o4XFOe1PO8jE3XTw?e=PA4Wcxv)
""")
elif consulta == opciones[1]:
    st.markdown("""
**Visualización del expediente digital como e-book:**  
[Guía paso a paso (OneDrive)](https://scbagovar-my.sharepoint.com/:b:/g/personal/rcsdellaporta_scba_gov_ar/EbL9wah_T_BEjdV8mPGDFQYBHdMX4V4xOhVtJK61Jf9dWQ?e=6FtcAG)
""")
elif consulta == opciones[2]:
    st.markdown("""
**Uso de TICs para testimoniales en procesos BLSG:**  
[Acceder a la guía (OneDrive)](https://scbagovar-my.sharepoint.com/:b:/g/personal/rcsdellaporta_scba_gov_ar/EZ8AXylbqQtPjMmQ_VBYJ9EB0Kkis9EPcmonM3ymYDVvTQ?e=WxhwAd)
""")
elif consulta == opciones[3]:
    st.markdown("""
**Redes sociales activas del juzgado:**  
Instagram: [@juzgado9civil](https://www.instagram.com/juzgado9civil/)  
*Facebook actualmente no se encuentra activo.*
""")
elif consulta == opciones[4]:
    st.markdown("""
**Encuestas de satisfacción:**  
[Encuesta para profesionales del Derecho](https://docs.google.com/forms/d/e/1FAIpQLSelQUyg_3rns4lk5lEhupU311yxPwfZDXspvreS-GwYnxrSWw/viewform)  
[Encuesta general de satisfacción](https://docs.google.com/forms/d/e/1FAIpQLSd3ILJSn6i2F-WXT85Ap_-3WWSyYZ6ULjqFFKgt0fc0dmqxiQ/viewform)
""")
elif consulta == opciones[5]:
    st.markdown("""
**SADyP - Servicio de Atención Digital y Personalizada**  
Disponible por Zoom, de lunes a viernes de 9 a 13 hs.  
[Acceder a la sala Zoom](https://us05web.zoom.us/j/4715183830?pwd=KzZlVUtjWnZlYlJyWmx2ZGFKTHdmZz09)
""")

st.markdown("""---  
✨ **Gracias por utilizar el Asistente Virtual IA del Juzgado Civil y Comercial N° 9.**  
Este servicio está en desarrollo continuo. Sus comentarios son bienvenidos.
""")
