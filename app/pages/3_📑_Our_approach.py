import base64
import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="Our Approach",
    page_icon="🔍",
)

#st.markdown(os.getcwd())


st.markdown("## 📄 Our Detailed Approach")
#pdf_file = "assets/FinalProject.pdf" 
#st.markdown("### 📘 Read our detailed PDF here:")

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display =  f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 100%;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def get_base64_of_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return data

def displayPDF2():
    # Ajout d'un lien vers un PDF
    pdf_file = "app/asset/Python_DIA1_ESTIGNARD_COCKENPOT_MELL_MARIOLLE.pdf"    
    pdf_base64 = get_base64_of_pdf(pdf_file)

    # Intégrer le PDF dans la page
    pdf_html = f'<embed src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf">'
    st.components.v1.html(pdf_html, height=1000)

st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3em;      /* Hauteur du bouton */
        width: 100%;      /* Largeur du bouton (100% de la largeur disponible) */
        font-size: 1.5em; /* Taille de la police */
        margin: 5px 0;    /* Marge au-dessus et en dessous du bouton */
    }
    /* Custom CSS pour supprimer le padding par défaut de Streamlit autour des widgets */
    .st-cx {
        padding: 0px;
    }
    </style>
""", unsafe_allow_html=True)

st.write("\n" * 15)

if st.button("📑 Detailed presentation", key="1"):
     displayPDF2()

if st.button("📊 Training dataset", key="2"):
    st.markdown("https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008")


if st.button("👨‍💻 GitHub", key="3"):
    st.markdown("https://github.com/FoucauldE/Project-Diabetes-130-US-hospitals-1999-2008")






