def evaluate_answer(answer):
    """
    Evaluate interview answer quality.
    """

    # Remove extra spaces
    answer = answer.strip()

    # Word Count
    word_count = len(answer.split())

    # Empty Answer Check
    if word_count == 0:

        return {
            "score": 0,
            "feedback": "❌ No answer provided."
        }

    # Very Short Answer
    elif word_count < 10:

        return {
            "score": 4,
            "feedback": "⚠ Answer is too short. Try explaining in more detail."
        }

    # Medium Quality Answer
    elif word_count < 30:

        return {
            "score": 7,
            "feedback": "✅ Good answer. You can improve it with more technical details."
        }

    # Strong Answer
    else:

        return {
            "score": 9,
            "feedback": "🔥 Excellent answer with good explanation and detail."
        }