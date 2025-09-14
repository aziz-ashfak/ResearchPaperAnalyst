import os
import streamlit as st
from src.utils.pdf_utils import extract_pdf_text, extract_pdf_images
from src.utils.llm_utils import explain_document, answer_followup, describe_image
from src.utils.export_utils import export_to_word, export_to_pdf

st.set_page_config(page_title="Multimodal Paper Analyzer", layout="wide")
st.title("📚 Multimodal Research Paper Analyzer")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    
    pdf_path  = "temp_uploaded.pdf"
  
    #pdf_path = os.makedirs(upload_dir, exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("PDF uploaded successfully!")

    with st.spinner("Extracting text..."):
        text = extract_pdf_text(pdf_path)

    with st.spinner("Summarizing with Groq..."):
        summary_prompt = (
            "Provide a detailed overview of the research paper, including: "
            "1. Literature review summary. "
            "2. Methodology. "
            "3. Results. "
            "4. Conclusion. "
            "Finally, add a complimentary comment."
        )
        summary = explain_document(text, summary_prompt)
        st.subheader("🧠 Research Summary")
        st.write(summary)

    with st.spinner("Extracting and analyzing figures..."):
        image_info = extract_pdf_images(pdf_path)
        figure_data = []
        for img_path, img_ext in image_info:
            caption = describe_image(img_path, img_ext)
            figure_data.append({"path": img_path, "caption": caption})

    st.subheader("🖼 Figures & Summaries")
    for fig in figure_data:
        st.image(fig["path"], caption=os.path.basename(fig["path"]), use_container_width=True)
        st.markdown(f"**Summary:** {fig['caption']}")

    st.subheader("❓ Ask a Follow-up Question")
    followup_question = st.text_input("Enter your question about the paper or figures:")
    if followup_question:
        with st.spinner("Analyzing your question..."):
            answer = answer_followup(text, followup_question)
            st.write("**Answer:**", answer)

    st.subheader("📤 Export Report")
    word_buffer = export_to_word(summary, figure_data)
    pdf_buffer = export_to_pdf(summary, figure_data)

    st.download_button("📥 Download Word Report", word_buffer.getvalue(), "summary.docx",
                       mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    st.download_button("📥 Download PDF Report", pdf_buffer.getvalue(), "summary.pdf", mime="application/pdf")
