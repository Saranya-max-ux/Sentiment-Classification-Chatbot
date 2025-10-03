# Import required libraries
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import string

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocesses the input text by:
    - converting to lowercase
    - removing punctuation
    - tokenizing
    - removing stopwords
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def analyze_sentiment(text):
    """
    Analyzes sentiment of preprocessed text using TextBlob.
    Returns: Positive, Negative, or Neutral
    """
    analysis = TextBlob(preprocess_text(text))
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def chatbot():
    """
    Runs the sentiment classification chatbot.
    Simulates business-aligned responses.
    """
    print("Hi! I'm your Feedback Bot. Type 'exit' to leave.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for your feedback! Goodbye!")
            break
        sentiment = analyze_sentiment(user_input)
        if sentiment == "Positive":
            print("Glad to hear that! Your feedback motivates us.")
        elif sentiment == "Negative":
            print("Sorry to hear that. We'll strive to improve.")
        else:
            print("Thanks for sharing your thoughts!")

if __name__ == "__main__":
    chatbot()
