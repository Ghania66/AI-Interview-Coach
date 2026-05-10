# Technical Interview Questions Database

QUESTION_DB = {

    "python": [
        "What is the difference between lists and tuples in Python?",
        "Explain list comprehension in Python.",
        "What are Python decorators?",
        "What is the difference between deep copy and shallow copy?"
    ],

    "machine learning": [
        "What is overfitting in machine learning?",
        "Explain supervised vs unsupervised learning.",
        "What is the bias-variance tradeoff?",
        "What are evaluation metrics in classification?"
    ],

    "sql": [
        "What is the difference between WHERE and HAVING?",
        "Explain SQL joins.",
        "What is normalization?",
        "What are primary and foreign keys?"
    ],

    "streamlit": [
        "Why is Streamlit useful for AI applications?",
        "Explain Streamlit session state.",
        "How do you deploy a Streamlit app?"
    ],

    "tensorflow": [
        "What is TensorFlow?",
        "Explain tensors in deep learning.",
        "What is backpropagation?"
    ],

    "opencv": [
        "What is image thresholding?",
        "Explain edge detection in OpenCV.",
        "What is contour detection?"
    ]
}


# HR Questions
HR_QUESTIONS = [

    "Tell me about yourself.",

    "Why should we hire you?",

    "What are your strengths and weaknesses?",

    "Describe a challenging project you worked on.",

    "Where do you see yourself in 5 years?"
]


def generate_questions(skills):
    """
    Generate interview questions based on skills.
    """

    generated_questions = []

    # Technical Questions
    for skill in skills:

        skill = skill.lower()

        if skill in QUESTION_DB:

            generated_questions.extend(
                QUESTION_DB[skill]
            )

    # Add HR Questions
    generated_questions.extend(HR_QUESTIONS)

    return generated_questions