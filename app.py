from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
style = diretorio / "style" / "style.css"
arquivo_pdf = diretorio / "assets" / "Profile.pdf"
arquivo_img = diretorio / "assets" / "foto.jpg"

# Configurações gerais das informações

TITULO = "Curriculum | Samuel Chiodini"
NOME = "Samuel Chiodini"
DESCRICAO = "Olá me chamo Samuel, tenho 22 anos. Possuo experiência prévia em eletrônica e atualmente trabalho na área de tecnologia como programador. Desde jovem, tenho grande interesse e dedicação pela computação, e sou muito cuidadoso e responsável com minhas tarefas. Levo meu trabalho a sério e mantenho a brincadeira em momentos apropriados. Prezo por manter uma postura educada com aqueles que convivem comigo e evitoconflitos desnecessários. Além disso, sou extremamente motivado para aprender coisas novas e aperfeiçoar minhas habilidades existentes."
EMAIL = "samuel@teste"
MIDIA_SOCIAL = {
    "Linkedin" : "https://www.linkedin.com/in/samuel-chiodini-5621931b3/",
    "GitHub" : "https://github.com/Samuca23"
}

CURSOS = {
    "☕ PHP" : "www.google.com.br"
}

st.set_page_config(
    page_title=TITULO
)

# Carregando assets
with open(style) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()

imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(imagem, width=250)
with col2:
    st.title(NOME);
    st.write(DESCRICAO);
    st.download_button(
        label="Download currículo",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-strem"
    )
    st.write("✉️ E-mail")

# Mídias sociais
st.write("#");
colunas = st.columns(len(MIDIA_SOCIAL))

for index, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[index].write(f"[{plataforma}]({link})")

#Experiencias
st.write("#")
st.subheader("Experiências")
st.write(
    """
        - 💹 2 Ano como programador PHP.
        - 💹 Conhecimento em Python.
        - 💹 Desenvolvimento web.
    """
)

#Skills
st.write("#");
st.subheader("Skills")
st.write(
    """
        - 💾 Revisão em Pares.
        - 📈 Auxílio de programadore novatos.
        - 💻 Bom comportamento.
    """
)