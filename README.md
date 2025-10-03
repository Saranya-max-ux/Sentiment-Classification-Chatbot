# Sentiment-Classification-Chatbot

A Python-based chatbot that analyzes real-time user feedback and classifies sentiment as Positive, Negative, or Neutral. Built using NLTK for text preprocessing and TextBlob for sentiment analysis, the chatbot provides business-aligned responses and simulates real-world customer interaction.

# Features

Real-time sentiment analysis of user input.

Classifies feedback as Positive, Negative, or Neutral.

Uses NLTK for tokenization, stopword removal, and text preprocessing.

Uses TextBlob for sentiment detection.

Business-aligned responses based on sentiment.

Ready for future enhancements with LLM/GenAI integration.

# Installation

Clone the repository:

git clone <your-repo-link>
cd <repo-folder>


# Install dependencies:

pip install nltk textblob
python -m textblob.download_corpora

# Usage

Run the chatbot:

python sentiment_chatbot.py


# Example interaction:

Hi! I'm your Feedback Bot. Type 'exit' to leave.
You: I love this product
Glad to hear that! Your feedback motivates us.
You: The service was slow
Sorry to hear that. We'll strive to improve.
You: exit
Thank you for your feedback! Goodbye!

# Future Enhancements

Logging feedback for analytics.

Integration with Flask/FastAPI for web deployment.

Use advanced NLP models like VADER or transformers for higher accuracy.

Integrate LLM/GenAI for personalized and context-aware responses.
