import fitz
import os
from config import IMAGE_DIR

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    return "".join([page.get_text() for page in doc])



def extract_pdf_images(pdf_path):
    """Extract images from a PDF and save them."""
    doc = fitz.open(pdf_path)
    image_paths = []
    for page_index in range(len(doc)):
        for img_index, img in enumerate(doc.get_page_images(page_index)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = os.path.join(
                IMAGE_DIR, f"page{page_index+1}_img{img_index+1}.{image_ext}"
            )
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            image_paths.append((image_path, image_ext))
    return image_paths


