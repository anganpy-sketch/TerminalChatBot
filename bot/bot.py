from google import genai

client = genai.Client(api_key="removed")

history = []

while 1:
    msg = input("You: ")

    if msg == "/exit":
        print("Bot: Bye!")
        break

    if msg == "/help":
        print("""
Commands:
/help    - show commands
/history - show chat history
/memory  - show number of stored messages
/save    - save chat to chat.txt
/load    - load chat from chat.txt
/clear   - clear chat memory
/exit    - quit bot
""")
        continue

    if msg == "/history":
        print("\n".join(history))
        continue

    if msg == "/memory":
        print(f"Messages stored: {len(history)}")
        continue

    if msg == "/save":
        with open("chat.txt", "w") as file:
            file.write("\n".join(history))

        print("Bot: Chat saved to chat.txt")
        continue

    if msg == "/load":
        with open("chat.txt", "r") as file:
            history = file.read().splitlines()

        print("Bot: Chat loaded from chat.txt")
        continue

    if msg == "/clear":
        history = []
        print("Bot: Memory cleared.")
        continue

    history.append("User: " + msg)

    conversation = "\n".join(history)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation
    )

    print("Bot:", response.text)

    history.append("Bot: " + response.text)