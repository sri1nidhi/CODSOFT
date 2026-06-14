import random

greetings = [
    "Hello! How can I help you?",
    "Hi there!",
    "Hey! Nice to meet you."
]

responses = {
    "name": "I am CodSoft AI Chatbot.",
    "how are you": "I am doing great! Thanks for asking.",
    "course": "I can help with AI, Python and Machine Learning topics.",
    "python": "Python is a popular programming language used in AI and Data Science.",
    "ai": "Artificial Intelligence enables machines to mimic human intelligence.",
    "bye": "Goodbye! Have a great day!"
}

print("=" * 40)
print("      RULE-BASED CHATBOT")
print("=" * 40)
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    elif "name" in user:
        print("Bot:", responses["name"])

    elif "how are you" in user:
        print("Bot:", responses["how are you"])

    elif "course" in user:
        print("Bot:", responses["course"])

    elif "python" in user:
        print("Bot:", responses["python"])

    elif "ai" in user:
        print("Bot:", responses["ai"])

    elif user == "bye":
        print("Bot:", responses["bye"])
        break

    else:
        print("Bot: Sorry, I don't understand that.")