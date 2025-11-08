def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thanks for asking! What about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        # Default response for unrecognized input
        return "I'm sorry, I didn't understand that. Could you rephrase?"
def start_chat():
    print("Chatbot: Hello! I am a simple rule-based bot. Type 'bye' to exit.")
    # Infinite loop to keep the conversation going
    while True:
        # Get input from the user
        user_input = input("You: ")
        # Check for exit commands
        if user_input.lower() in ['bye', 'quit', 'exit']:
            print("Chatbot: Goodbye!")
            break # Exit the loop
        # Get and print the chatbot's response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
# This line ensures the function runs when the script is executed
if __name__== "__main__":
    start_chat()
