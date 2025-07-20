import nltk
import random
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')  # Also needed for lemmatization
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required resources (only first time)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')  # For lemmatizer

# Sample corpus for the chatbot
corpus = """
hi
Hello! How can I assist you?

hello
Hi there! How can I help you?

how are you
I'm just a bot, but I'm doing well. Thanks for asking!

what is your name
I'm a chatbot created with Python and NLTK.

what can you do
I can answer basic questions and chat with you.

tell me a joke
Why don’t scientists trust atoms? Because they make up everything!

what is python
Python is a high-level, interpreted programming language.

who created you
I was created by a Python programmer using Natural Language Processing.

bye
Goodbye! Have a great day!

thank you
You're welcome!

thanks
Anytime!

how is the weather
I'm not connected to live weather data, but I hope it's sunny!

what is machine learning
Machine learning is a field of artificial intelligence that teaches computers to learn from data.

what is AI
AI stands for Artificial Intelligence, which enables machines to mimic human behavior.

what is your purpose
I'm here to help you with basic questions and have a conversation.

do you know any programming languages
Yes! I was created using Python.

what is NLP
NLP stands for Natural Language Processing. It's used to help computers understand human language.

how old are you
I don't have an age like humans do. I exist as code!

can you help me
Of course! What do you need help with?

what are you doing
I'm just here waiting to chat with you!
"""

# Tokenization
sent_tokens = nltk.sent_tokenize(corpus.lower())

# Lemmatization
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greeting inputs and responses
GREETING_INPUTS = ("hello", "hi", "hey", "greetings")
GREETING_RESPONSES = ["hi", "hello there", "hey!", "hi, how can I help?"]

def greeting(sentence):
    """Return a greeting if user's input is a greeting"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate chatbot response
def generate_response(user_input):
    user_input = user_input.lower()
    sent_tokens.append(user_input)

    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = vectorizer.fit_transform(sent_tokens)
    similarity_scores = cosine_similarity(tfidf[-1], tfidf)

    idx = similarity_scores.argsort()[0][-2]
    flat = similarity_scores.flatten()
    flat.sort()
    score = flat[-2]

    sent_tokens.pop()  # Clean up

    if score == 0:
        return "I'm sorry, I didn't quite understand that."
    else:
        return sent_tokens[idx]

# Run chatbot
print("BOT: Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("YOU: ")
    if user_input.lower() == 'bye':
        print("BOT: Goodbye! Have a nice day.")
        break
    elif greeting(user_input):
        print("BOT:", greeting(user_input))
    else:
        print("BOT:", generate_response(user_input))
