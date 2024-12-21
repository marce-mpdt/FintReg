import streamlit as st
import smtplib
from PIL import Image
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Configuración de la página
st.set_page_config(page_title="FintReg Asesoría Regulatoria", page_icon="logo_empresa.png", layout="wide")

# Agregar el logo
st.image("logo_empresa.png", width=200)  # Asegúrate de tener el archivo "logo_empresa.png" en la misma carpeta



# Aplicar estilo personalizado con CSS
st.markdown(
    """
    <style>
    /* Fondo con tonos azules translúcidos */
    .stApp {
        background: linear-gradient(135deg, rgba(0, 123, 255, 0.5), rgba(0, 200, 255, 0.5));
        background-attachment: fixed;
        color: white;
    }
    /* Estilo para el pie de página */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: rgba(0, 123, 255, 0.7);
        padding: 10px 0;
        text-align: center;
        color: white;
    }
    .footer a {
        color: #FFD700;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Título del banner
st.title("¿Necesitas ayuda con la solicitud de inscripción o autorización de prestación de servicios Fintech?")

# Cargar imagen desde la misma carpeta
image_path = "banner.png"  # Reemplaza con el nombre exacto de tu imagen
img_1 = Image.open(image_path)

#cargar imagen foto mia
image_path2 = "foto.png"  # Reemplaza con el nombre exacto de tu imagen
img_2 = Image.open(image_path2)

#cargar imagen foto 
image_path3 = "banner2.png"  # Reemplaza con el nombre exacto de tu imagen
img_3 = Image.open(image_path3)

# Imagenes para columnas
img1 = Image.open("1.png")
img2 = Image.open("2.png")
img3 = Image.open("3.png")
img4 = Image.open("4.png")
img5 = Image.open("5.png")
img6 = Image.open("6.png")
img7 = Image.open("7.png")


# Mostrar imagen y texto
with st.container():
    st.write("---")
    col1, col2 = st.columns((4,1))
    with col1:
        st.image(img_1, caption="***Dedicate a lo que sabes hacer, y el resto lo resolvemos juntos***", use_container_width=True)
    with col2:
    
        st.header("""
            ¿No sabes por dónde empezar?\n
            

        """)
        st.header("""
                ¿Abrumado con la regulación? \n

        """)

    st.header("Explora nuestras soluciones y encuentra lo que necesitas.")

# Menú de navegación
#menu = st.sidebar.radio("Navegación", ["Inicio", "Sobre las Fintec", "Planes", "Contacto"])

# Sección: Inicio
#if menu == "Inicio":
with st.container():    
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img_2)
        
    with col2:
        
        
        st.subheader(
            """
            Nuestra especialista en cumplimiento regulatorio y mercados financieros. Ingeniera Comercial con Magíster en Finanzas y Diplomado en Data Science, con más de quince años de experiencia profesional y con más de nueve años de experiencia fiscalizando corredoras de bolsa y agentes de valores."

            """
        )
        st.write("---")
        st.subheader(
            """
            Nuestro objetivo es proporcionar asesorías de calidad y personalizadas para el cumplimiento regulatorio en el sector Fintech y mantener una relación eficiente con el regulador.
        """
        )
        st.header(
            """
            Seguramente te podré ayudar en:
         """
        )
        
        st.subheader(
            """
            - ***Asesoría de Inscripción***: Te ayudamos con el proceso de inscripción ante entidades regulatorias.
            
                 """
        )
        st.subheader(
            """
            
            - ***Asesoría de Autorización Prestación Servicios***: Te asesoramos para que cumplas con todos los requisitos legales.
         
                 """
        )  
        st.subheader(
            """
           
            - ***Gestión de Riesgos Regulatorios***: Identificación, evaluación y mitigación de los riesgos asociados al cumplimiento regulatorio 
                 """
        )
        st.write("---")
st.header(
            """
            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
                """
        )

# Sección: Todo sobre las Fintech
#elif menu == "Sobre las Fintec":    
with st.container():    
    st.write("---")
    st.header("Lo que hay que saber sobre Fintech")
    st.subheader("En enero de 2023 se publicó la Ley N°21.521 (Ley Fintec) cuyo objetivo general es promover la competencia e inclusión financiera a través de la innovación y tecnología en la prestación de servicios financieros.")
    st.header("¿Qué son las Fintech?")
    st.subheader("Las Fintech son empresas que utilizan herramientas tecnológicas para ofrecer servicios financieros innovadores.")
    st.subheader("Las Fintech están reguladas bajo ciertas normativas para proteger a los consumidores y promover la transparencia.")
    
    st.header("Servicios Financieros")
    st.image(img_3, caption="***Servicios Financieros***", use_container_width=True)

    # CSS personalizado para mantener los contenedores uniformes
with st.container():
    st.write("---")
    st.header("Servicios Financieros")
    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img1, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            Servicio ofrecido por personas naturales o entidades especializadas que brindan evaluaciones o recomendaciones a terceros respecto de la conveniencia de realizar determinadas inversiones u operaciones en valores de oferta pública, instrumentos financieros o proyectos de inversión. Este servicio no comprende las asesorías previsionales, ni las actividades de los agentes de ventas de compañías de seguros.    
            """
        )

    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img2, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            En este servicio se ofrecen evaluaciones o recomendaciones a terceros respecto de la capacidad o probabilidad de pago de personas o entidades, con el fin de la obtener, modificar o renegociar créditos o financiamientos.    
            """
        )   

    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img3, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            También conocidas como plataformas de crowdfunding, el servicio consiste en la creación de un lugar físico o virtual por medio del cual personas o empresas que necesitan dinero para sus proyectos los presentan al público. Estas plataformas no solo conectan a quienes buscan financiamiento con quienes desean invertir, sino que también ofrecen servicios adicionales.
            """
        ) 
    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img4, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            El servicio consiste en la creación de un lugar físico o virtual que permite a sus participantes cotizar, ofrecer o transar instrumentos financieros y que no está autorizado para actuar como bolsa de valores o bolsa de productos.
            """
        ) 

    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img5, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            Este servicio consiste en recibir y dirigir órdenes de terceros para la compra o venta de instrumentos financieros canalizándolas hacia sistemas alternativos de transacción, intermediarios de valores o corredores de bolsas de productos.
            """
        )            
    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img6, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            El servicio consiste en que las entidades participantes realizan la compra o venta de instrumentos financieros para terceros, las cuales se hacen adquiriendo o enajenando por cuenta propia instrumentos financieros, cuando exista el ánimo anterior de vender o comprar esos mismos instrumentos al tercero, o bien, adquiriendo o vendiendo instrumentos financieros en nombre de o para dicho tercero.
            """
        )  
    st.write("##")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(img7, use_container_width=True)
    with text_column:
        st.subheader(
        
            """
            El servicio consistente en la custodia y protección de activos financieros, como acciones, bonos, o títulos de deuda en nombre de sus dueños. Así las instituciones que participan en este mercado se encargan de conservar estos activos de forma segura, garantizando de que estén registrados y administrados de forma correcta
            """
        ) 
    
with st.container():   
    st.write("---")
    st.header("Normativa y Regulación")
    st.subheader("Las Fintech deben cumplir con regulaciones locales relacionadas con la protección de datos y la prevención del lavado de dinero.")
    
    st.header("Instituciones que Participan")
    st.subheader("En Chile, instituciones como la Comisión para el Mercado Financiero (CMF) supervisan las operaciones de las Fintech.")
    st.markdown("[Más información en CMF](https://www.cmfchile.cl/portal/principal/613/w3-propertyvalue-43589.html")
    st.markdown("[y también en CMF Educa](https://www.cmfeduca.cl/educa/621/w3-propertyvalue-48145.html)")

# # Sección: Planes
# #elif menu == "Planes":
# with st.container():    
#     st.write("---")
#     st.header("Nuestros Planes")
#     st.subheader("Creamos soluciones personalizadas para cada cliente:")
#     st.markdown("- **Plan Básico** Agenda una hora y resuelve todas las dudas que tengas.")
#     st.markdown("- **Plan Pro:** Revisión de documentos con feedback, más llamadas telefónicas o reuniones para resolver dudas.")
#     st.markdown("- Cotiza el producto que te hace falta personalizado")

st.markdown(
    """
    <style>
    /* Estilo para el texto de los planes */
    .custom-plans {
        color: #003366; /* Azul oscuro */
        font-size: 20px; /* Tamaño header */
        font-weight: bold; /* Negrita */
        line-height: 1.6; /* Espaciado entre líneas */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sección "Planes"
with st.container():
    st.write("---")
    st.header("Nuestros Planes")
    st.markdown('<div class="custom-plans">- <strong>Plan Básico</strong>: Agenda una hora y resuelve todas las dudas que tengas.</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-plans">- <strong>Plan Pro</strong>: Revisión de documentos con feedback, más llamadas telefónicas o reuniones para resolver dudas.</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-plans">- <strong>Plan Personalizado</strong>: Cotiza el producto que necesitas según las necesidades específicas de tu empresa.</div>', unsafe_allow_html=True)

# Sección: Contacto
#elif menu == "Contacto":
with st.container():    
    st.write("---")
    st.header("Contáctanos")
    st.write("¡Estamos aquí para ayudarte! Completa tus datos:")

    # Captura de datos del usuario
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo Electrónico")
    mensaje = st.text_area("Mensaje")


    if st.button("Enviar"):
        if nombre and correo and mensaje:
            try:
                # Configuración del correo
                remitente = "fintreg.cl@gmail.com"  # Cambia a un correo válido (usa una cuenta SMTP activa)
                password = "Kucu abfe tffg soaa"  # Contraseña del remitente
                destinatario = "fintreg.cl@gmail.com"
                asunto = f"Mensaje de {nombre} desde la página web"

                # Crear el contenido del correo
                msg = MIMEMultipart()
                msg['From'] = remitente
                msg['To'] = destinatario
                msg['Subject'] = asunto
                cuerpo = f"Nombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"
                msg.attach(MIMEText(cuerpo, 'plain'))

                # Enviar el correo
                servidor = smtplib.SMTP('smtp.gmail.com', 587)
                servidor.starttls()
                servidor.login(remitente, password)
                servidor.send_message(msg)
                servidor.quit()

                st.success("Mensaje enviado exitosamente.")
                # Limpiar campos
                st.session_state["nombre"] = ""
                st.session_state["correo"] = ""
                st.session_state["mensaje"] = ""
                st.experimental_rerun()  # Reinicia la interfaz
            except Exception as e:
                st.error(f"Error al enviar el mensaje: {e}")
        else:
            st.warning("Por favor, completa todos los campos.")

# Agregar el estilo CSS para el botón "Enviar"
st.markdown(
    """
    <style>
    /* Botón personalizado */
    div.stButton > button {
        background-color: #003366; /* Azul oscuro */
        color: white; /* Texto blanco */
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    div.stButton > button:hover {
        background-color: #002244; /* Azul más oscuro al pasar el ratón */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Información de contacto y redes sociales en el pie de página
st.markdown(
    """
    <div class="footer">
        <p>Contacto: <a href="mailto:fintreg.cl@gmail.com">fintreg.cl@gmail.com</a></p>
        <p>Síguenos en:
            <a href="https://www.linkedin.com/in/marcela-paz-ma%C3%B1as-p%C3%A9rez-de-tudela-81455252?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">LinkedIn</a> |
            <a href="https://www.instagram.com/fintreg.cl?igsh=NHQ2ZWtjOHZ6Ynp1" target="_blank">Instagram</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)   
