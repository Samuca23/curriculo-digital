from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais
diretorio = Path(__file__).paret if "__file__" in locals() else Path.cwd()
style = diretorio / "style" / "style.css"
arquivo_pdf = diretorio / "assets" / "Profile.pdf"
arquivo_img = diretorio / "assest" / "foto.jpg"

# Configurações gerais das informações

TITULO = "Curriculum | Samuel Chiodini"
NOME = "Samuel Chiodini"
DESCRICAO = "'"
EMAIL = "samuel@teste"
MIDIA_SOCIAL = {
    "Linkedin" : "https://www.linkedin.com/in/samuel-chiodini-5621931b3/",
    "GitHub" : "https://github.com/Samuca23"
}

CURSOS = {
    "☕ PHP" : "www.google.com.br"
}