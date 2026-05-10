import streamlit as st

from utils.resume_parser import (
    extract_resume_text,
    extract_skills
)

from utils.question_generator import generate_questions

from utils.feedback_engine import evaluate_answer


# Page Configuration
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Interview Coach")

st.markdown("""
Upload your resume and get AI-powered interview preparation.
""")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

# PROCESS RESUME
if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Extract Resume Text
    resume_text = extract_resume_text(uploaded_file)

    # Extract Skills
    skills = extract_skills(resume_text)

    # Generate Questions
    questions = generate_questions(skills)

    # Display Resume Text
    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    # Display Skills
    st.subheader("🧠 Detected Skills")

    if skills:

        for skill in skills:
            st.success(skill)

    else:
        st.warning("No skills detected.")

    # Interview Questions
    st.subheader("🎯 Interview Questions")

    for index, question in enumerate(questions, start=1):

        st.subheader(f"Question {index}")

        st.info(question)

        # Answer Input
        user_answer = st.text_area(
            f"Your Answer for Question {index}",
            key=f"answer_{index}"
        )

        # Evaluate Button
        if st.button(f"Evaluate Answer {index}"):

            result = evaluate_answer(user_answer)

            st.write(f"⭐ Score: {result['score']}/10")

            st.success(result["feedback"])