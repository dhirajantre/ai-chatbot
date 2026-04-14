print("🤖 Simple Chatbot Started (type 'exit' to stop)\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye! 👋")
        break

    elif "hello" in user:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am your AI chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine, thanks!")

    elif "cybersecurity" in user:
        print("Bot: Cybersecurity is about protecting systems and data from hackers.")

    else:
        print("Bot: Sorry, I didn't understand that.")