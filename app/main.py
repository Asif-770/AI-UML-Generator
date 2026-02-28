import streamlit as st
import sys
import os
import time

# Ensure the root directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.nlp.clean_text import clean_srs_text
from src.nlp.parser import SRSParser
from src.nlp.extractor import UMLExtractor
from src.logic.classifier import RelationshipClassifier
from src.generators.plantuml import PlantUMLGenerator
from src.generators.xmi import XMIGenerator
from src.utils.graph_ui import render_interactive_graph

# --- Page Configuration ---
st.set_page_config(page_title="UML Generator Pro", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for Modern Tabs & Footer ---
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
        background-color: #1F2937;
        border: 1px solid #374151;
        border-bottom: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3B82F6;
        color: #ffffff !important;
        font-weight: bold;
    }
    .custom-footer {
        text-align: center;
        color: #9CA3AF;
        font-size: 14px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #374151;
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
if 'extracted' not in st.session_state:
    st.session_state.extracted = False
if 'components' not in st.session_state:
    st.session_state.components = {"classes": [], "attributes": [], "methods": []}
if 'relationships' not in st.session_state:
    st.session_state.relationships = []
if 'srs_text' not in st.session_state:
    st.session_state.srs_text = "The Library Management System shall allow a User to borrow books.\nA Librarian is a User.\nThe Library contains Books."

# --- Cached NLP Model Loading ---
@st.cache_resource
def load_parser():
    return SRSParser()

parser = load_parser()
extractor = UMLExtractor()
classifier = RelationshipClassifier()
puml_gen = PlantUMLGenerator()
xmi_gen = XMIGenerator()

# ==========================================
# ADVANCED SIDEBAR: Engine Control
# ==========================================
with st.sidebar:
    # Restored Logo and Color Code
    st.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <img src='https://img.icons8.com/nolan/96/artificial-intelligence.png' width='70'>
            <h2 style='color: #00E5FF; text-transform: uppercase; letter-spacing: 2px; font-size: 20px; margin-top: 10px;'>Engine Control</h2>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # --- 1. Data Ingestion ---
    with st.expander("📂 DATA INGESTION", expanded=True):
        uploaded_file = st.file_uploader("Upload Document (.txt, .md)", type=["txt", "md"])
        if uploaded_file is not None:
            string_data = uploaded_file.getvalue().decode("utf-8")
            st.session_state.srs_text = string_data
            st.success("Buffer loaded.")

        user_input = st.text_area("Requirements Input:", value=st.session_state.srs_text, height=200)

    # --- 2. Advanced NLP Settings ---
    with st.expander("🔧 NLP HYPERPARAMETERS", expanded=False):
        st.slider("Confidence Threshold", min_value=0.50, max_value=1.00, value=0.85, step=0.05, 
                  help="Adjust how strict the AI is when identifying relationships.")
        st.toggle("Strict Inheritance Mode", value=True, help="Only use 'is a' exact lexical matching.")
        st.selectbox("Processing Engine", ["spaCy en_core_web_sm (Fast)", "Transformers (Pro Only)"], disabled=True)
        st.caption("Upgrade your plan to unlock transformer-based extraction.")

    st.markdown("---")
    
    # --- 3. Execution & Memory Controls ---
    col1, col2 = st.columns([4, 1])
    with col1:
        extract_btn = st.button("🚀 INITIATE EXTRACTION", type="primary", use_container_width=True)
    with col2:
        reset_btn = st.button("🗑️", help="Purge Session Memory")
        
    if reset_btn:
        st.session_state.extracted = False
        st.session_state.components = {"classes": [], "attributes": [], "methods": []}
        st.session_state.relationships = []
        st.rerun()

    if extract_btn:
        if not user_input.strip():
            st.error("Input buffer empty.")
        else:
            with st.status("Initializing NLP Pipeline...", expanded=True) as status:
                st.write("Sanitizing text buffer...")
                cleaned_text = clean_srs_text(user_input)
                time.sleep(0.3)
                
                st.write("Loading semantic parser...")
                doc = parser.parse(cleaned_text)
                
                st.write("Extracting component entities...")
                st.session_state.components = extractor.extract_components(doc)
                time.sleep(0.3)
                
                st.write("Mapping relational topologies...")
                st.session_state.relationships = classifier.classify_relationships(doc, st.session_state.components['classes'])
                
                st.session_state.extracted = True
                status.update(label="Extraction Complete!", state="complete", expanded=False)

    # --- SIDEBAR FOOTER ---
    st.markdown("<br><br><br>", unsafe_allow_html=True) # Push to bottom
    st.markdown("<div class='custom-footer'>Project created by<br><b>Md Asif Khan</b><br>Roll Num: 10830622038</div>", unsafe_allow_html=True)

# ==========================================
# MAIN DASHBOARD AREA
# ==========================================
st.title("System Architecture Visualizer")

if not st.session_state.extracted:
    st.info("👈 System idle. Awaiting data ingestion and extraction protocol from the Engine Control panel.")
    
    st.markdown("""
        ### Welcome to the UML Generator Pro
        This environment uses advanced natural language processing heuristics to transform plain English software requirements into structured architectural models.
        
        **Workflow:**
        1. **Ingest:** Upload a `.txt` file or paste raw text into the sidebar terminal.
        2. **Configure:** Tweak NLP hyperparameters in the settings menu.
        3. **Execute:** Initiate the extraction sequence.
        4. **Analyze:** Interact with the generated physics-based node graph.
        5. **Deploy:** Export raw PlantUML and XMI code for your IDE.
    """)
else:
    st.subheader("📊 Architecture Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Classes Identified", len(st.session_state.components['classes']))
    m2.metric("Attributes Found", len(st.session_state.components['attributes']))
    m3.metric("Methods Found", len(st.session_state.components['methods']))
    m4.metric("Relationships Mapped", len(st.session_state.relationships))
    
    st.markdown("---")
    
    col_graph, col_data = st.columns([2, 1])
    
    with col_graph:
        st.subheader("🕸️ Interactive Graph")
        with st.container(border=True):
            render_interactive_graph(st.session_state.components['classes'], st.session_state.relationships)

    with col_data:
        st.subheader("🧩 Structured Data")
        with st.expander("View Classes", expanded=True):
            for cls in st.session_state.components['classes']:
                st.markdown(f"- `{cls}`")
                
        with st.expander("View Attributes & Methods"):
            st.write("**Attributes:**")
            if st.session_state.components['attributes']:
                st.code("\n".join([f"{c}.{a}" for c, a in st.session_state.components['attributes']]))
            else:
                st.write("*None detected*")
                
            st.write("**Methods:**")
            if st.session_state.components['methods']:
                st.code("\n".join([f"{c}.{m}()" for c, m in st.session_state.components['methods']]))
            else:
                st.write("*None detected*")
            
        with st.expander("View Relationships"):
            if st.session_state.relationships:
                for s, r, t in st.session_state.relationships:
                    color = "#10B981" if r == "Inheritance" else "#3B82F6"
                    st.markdown(f"`{s}` <span style='color:{color}; font-weight:bold;'>--[{r}]--></span> `{t}`", unsafe_allow_html=True)
            else:
                st.write("*No relationships mapped.*")

    st.markdown("---")
    st.header("💾 Code Export")
    
    puml_code = puml_gen.generate_puml(
        st.session_state.components['classes'], 
        st.session_state.components['attributes'], 
        st.session_state.components['methods'], 
        st.session_state.relationships
    )
    
    xmi_code = xmi_gen.generate_xmi(
        st.session_state.components['classes'], 
        st.session_state.components['attributes'], 
        st.session_state.components['methods'], 
        st.session_state.relationships
    )
    
    tab_puml, tab_xmi = st.tabs(["PlantUML (.puml)", "XMI (.xml)"])
    
    with tab_puml:
        st.code(puml_code, language="plantuml")
        st.download_button("Download .puml", data=puml_code, file_name="architecture.puml", mime="text/plain", use_container_width=True)
        
    with tab_xmi:
        st.code(xmi_code, language="xml")
        st.download_button("Download .xmi", data=xmi_code, file_name="architecture.xmi", mime="application/xml", use_container_width=True)

# --- MAIN PAGE FOOTER ---
st.markdown("<div class='custom-footer'>Project created by <b>Md Asif Khan</b> (Roll Num: 10830622038)</div>", unsafe_allow_html=True)