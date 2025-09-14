from setuptools import setup, find_packages

setup(
    name="multimodal_paper_analyzer",
    version="0.1.0",
    author="Your Name",
    author_email="azizashfak@gmail.com",
    description="A multimodal research paper analyzer with PDF summarization, figure extraction, and LLM integration.",
    
    #url="https://github.com/yourusername/multimodal-paper-analyzer",  # optional
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[ ]
)
