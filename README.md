# ⚡ AI-Powered UML Generator Pro

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://asif-uml-generator.streamlit.app/)

**Project created by Md Asif Khan**

An advanced, NLP-driven application that automatically transforms plain English Software Requirements Specifications (SRS) into interactive, structured UML Class Diagrams. Built for developers, software architects, and students to rapidly prototype system architectures directly from text.

## 🚀 Live Demo
Access the live application here: [AI-Powered UML Generator Pro](https://asif-uml-generator.streamlit.app/)

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

## 📂 Folder Structure

```text
AI-UML-Generator/
├── app/
│   └── main.py              # Streamlit UI dashboard
├── src/                     # Core Backend Logic
│   ├── generators/          # PlantUML & XMI code generators
│   ├── logic/               # NLP Relationship classifier
│   ├── nlp/                 # spaCy parsers and text extractors
│   └── utils/               # Interactive graph UI logic
├── requirements.txt         # Python dependencies
├── .gitignore               # Files to ignore in repo
└── README.md                # You're reading it!

## 💻 Local Installation & Setup

If you wish to run this project locally on your machine, follow these steps:

git clone [https://github.com/Asif-770/AI-UML-Generator.git](https://github.com/Asif-770/AI-UML-Generator.git)
cd AI-UML-Generator
python -m venv my_env
my_env\Scripts\activate
pip install -r requirements.txt
streamlit run app/main.py