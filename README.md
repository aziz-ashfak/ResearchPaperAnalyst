# 📑 Multimodal Research Paper Analyst (RAG-Powered)

A **Multimodal RAG (Retrieval-Augmented Generation) system** for analyzing research papers.  
This tool can **summarize scientific papers**, **analyze graphs & images in PDFs**, and **generate structured reports** in Word and PDF formats.

---

## 🚀 Features
- 📄 **Summarize Research Papers** – Extract core ideas, contributions, and results.
- 🧠 **RAG-based Question Answering** – Ask specific queries about uploaded PDFs.
- 📊 **Graph & Image Analysis** – Interpret figures, charts, and diagrams inside papers.
- 📝 **Export Reports** – Save structured outputs in:
  - Word (`.docx`)
  - PDF (`.pdf`)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/aziz-ashfak/ResearchPaperAnalyst.git>
   cd <ResearchPaperAnalyst>
   ```

2. Create a virtual environment & install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)

   pip install -r requirements.txt
   ```
3. Uapdate .env file 
   ```bash
   update your .env with GROQ_API_KEY
   ```
4. Run the app locally with streamlit :
   ```bash
    streamlit run app.py
 ```

## Project Structure

```bash
├── extract_images  # extracted images from research paper 
├── research 
    ├── research(RAg).ipynb   # Jupyter notebooks for RAG experimentation.
├── src  # Core source code.
    ├── pipeline  # Q&A pipeline and utilities ( LLM interactions, PDF processing)
            ├── __init__.py 
            ├── helper.py      # main file of mutlimodal rag
            ├── prompts.py      # prompts for mutlimodal rag
        ├── utils
            ├── _init__.py
            ├── export_utils.py      #  all export function
            ├── llm_utils.py         # llm details for  mutimodal rag
            ├── pdf_utils.py         # extract text with images
├── config.py       # add Groq api key

├── .gitignore             
├── LICENSE                                
├── app.py       # app details with streamlit 
├── logger.py 
├── README.md          
├── requirements.txt   # installation details   
└── setup.py           # setup details
```

## 🎯 Usage
1. Upload a **PDF research paper**.   
2. Get **summarized insights** in the web app.  
3. Ask **custom queries** about the paper.  
4. Download results in **Word / PDF / CSV / Markdown**.

---

## 📊 Example Use Cases
- Students writing **literature reviews**  
- Researchers managing large sets of papers  
- Analysts generating **structured paper summaries**  
- Automated **graph/image interpretation** from scientific PDFs  

---

## 📜 License
MIT License © 2025 [Aziz Ashfak]

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and open a PR 🚀

---

## 🌟 Acknowledgements
# Acknowledgement 
![Multimodal(Rag)](https://img.shields.io/badge/Multimodal%2BRAG-blue) 
![LLMs](https://img.shields.io/badge/LLMs%20-orange)
![Prompt Engineering](https://img.shields.io/badge/Prompt%20Engineering-red)
![Groq](https://img.shields.io/badge/Groq%20-Llama-blue)
![Llama](https://img.shields.io/badge/Paper%20-Analysis-blue)
![Streamlit](https://img.shields.io/badge/Streamlit%20App-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
---
 
## Author

👤 **Aziz Ashfak**  
📧 Email: [azizashfak@gmail.com](mailto:azizashfak@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/aziz-ashfak](https://www.linkedin.com/in/aziz-ashfak1/)  
🐙 GitHub: [github.com/aziz-ashfak](https://github.com/aziz-ashfak/) 
