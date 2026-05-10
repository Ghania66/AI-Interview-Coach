import pdfplumber
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined Skills Database
SKILLS_DB = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "opencv",
    "streamlit",
    "sql",
    "mysql",
    "mongodb",
    "data science",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "github",
    "flask",
    "fastapi",
    "pandas",
    "numpy"
]


def extract_resume_text(uploaded_file):
    """
    Extract text from uploaded PDF resume.
    """

    extracted_text = ""

    try:
        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

        return extracted_text

    except Exception as e:
        return f"Error extracting resume text: {e}"


def extract_skills(resume_text):
    """
    Extract skills from resume text.
    """

    detected_skills = []

    # Convert text to lowercase
    resume_text = resume_text.lower()

    # Process text using spaCy
    doc = nlp(resume_text)

    # Extract tokens
    tokens = [token.text for token in doc]

    # Match skills
    for skill in SKILLS_DB:

        if skill.lower() in resume_text:
            detected_skills.append(skill)

    return list(set(detected_skills))