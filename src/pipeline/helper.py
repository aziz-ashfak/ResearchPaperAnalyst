#test the pipeline 

import os
from src.utils.pdf_utils import extract_pdf_text, extract_pdf_images
from src.utils.llm_utils import explain_document, answer_followup, describe_image
from src.utils.export_utils import export_to_word, export_to_pdf
import sys
import base64

def finalize_analysis(pdf_path, followup_question=None):
    # --- Extract text ---
    print("📖 Extracting text...")
    text = extract_pdf_text(pdf_path)

    # --- Summarize with LLM ---
    print("🧠 Generating research summary...")
    summary_prompt = (
        "Provide a detailed overview of the research paper, including: "
        "1. Literature review summary. "
        "2. Methodology. "
        "3. Results. "
        "4. Conclusion. "
        "Finally, add a complimentary comment."
    )
    summary = explain_document(text, summary_prompt)
    print("\n=== Research Summary ===\n")
    print(summary)

    # --- Extract & analyze figures ---
    print("\n Extracting and analyzing figures...")
    image_info = extract_pdf_images(pdf_path)
    figure_data = []
    for img_path, img_ext in image_info:
        caption = describe_image(img_path, img_ext)
        figure_data.append({"path": img_path, "caption": caption})
        print(f"\n[Figure: {os.path.basename(img_path)}]")
        print(f"Summary: {caption}")

    # --- Follow-up QnA ---
    if followup_question:
        print("\n Follow-up Question:", followup_question)
        answer = answer_followup(text, followup_question)
        print("Answer:", answer)

    # --- Export reports ---
    print("\n Exporting reports...")
    word_buffer = export_to_word(summary, figure_data)
    pdf_buffer = export_to_pdf(summary, figure_data)

    with open("test_result/summary.docx", "wb") as f:
        f.write(word_buffer.getvalue())

    with open("test_result/summary.pdf", "wb") as f:
        f.write(pdf_buffer.getvalue())

    print(" Reports saved: summary.docx, summary.pdf")

# for results directory
import os
os.makedirs("test_result", exist_ok=True)



if __name__ == "__main__":
    # Replace with your test PDF
    pdf_file = "C:\\MultimodalRAg\\Human_Segmentation_Research.pdf"
    followup_q = "What are the main contributions of this paper?"
    finalize_analysis(pdf_file, followup_q)
