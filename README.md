# ⚡ AI-Powered UML Generator Pro

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_URL_HERE)

**Project created by Md Asif Khan (Roll Num: 10830622038)**

An advanced, NLP-driven application that automatically transforms plain English Software Requirements Specifications (SRS) into interactive, structured UML Class Diagrams. Built for developers, software architects, and students to rapidly prototype system architectures directly from text.

## 🚀 Live Demo
Access the live application here: [AI-Powered UML Generator Pro](YOUR_STREAMLIT_APP_URL_HERE)

## ✨ Key Features
* **Natural Language Processing (NLP):** Utilizes `spaCy` dependency parsing and rule-based heuristics to intelligently identify classes, attributes, methods, and relationships from raw text.
* **Interactive Architecture Graph:** Features a draggable, pannable, physics-enabled network graph using `streamlit-agraph` to explore the generated neural topology in real-time.
* **Automated Code Export:** Instantly compiles the extracted architecture into standard **PlantUML (`.puml`)** and **XML Metadata Interchange (`.xmi`)** formats, ready to be imported into enterprise IDEs and modeling tools.
* **Modern Control Dashboard:** A sleek, enterprise-grade user interface with execution telemetry, dynamic metrics, and hyperparameter controls.

## 🛠️ Technology Stack
* **Frontend UI:** Streamlit, Streamlit-Agraph
* **NLP Engine:** spaCy (`en_core_web_sm`)
* **Core Logic & Extraction:** Python 3.x, scikit-learn
* **Graph Rendering:** NetworkX, vis.js

## 💻 Local Installation & Setup

If you wish to run this project locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME