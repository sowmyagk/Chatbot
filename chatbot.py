import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"how are you", ["I'm good, thanks for asking!", "I'm doing great!"]],
    [r"what is your name", ["I am a simple chatbot.", "You can call me ChatBot!"]],
    # Removed "bye" from pairs to prevent duplicate messages
]

chatbot = Chat(pairs, reflections)

print("Hello! I'm your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a nice day!")  # Prints only ONE goodbye message
        break  # Exits immediately

    response = chatbot.respond(user_input)

    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: I don't understand that.")
