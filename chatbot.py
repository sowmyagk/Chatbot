import nltk
from nltk.chat.util import Chat, reflections

responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I'm good, thanks for asking!",
    "what is your name": "I am a simple chatbot.",
    "bye": "Goodbye! Have a nice day!"
}

while True:
    user_input = input("You: ").strip().lower()

    if user_input in responses:
        print(f"Chatbot: {responses[user_input]}")
    elif user_input == "":  # Handle empty inputs
        print("Chatbot: Please say something.")
    else:
        print("Chatbot: I don't understand that.")

    if user_input == "bye":
        break
