from google import genai

client = genai.Client(api_key="Your api key here")

history = []

while 1:
	msg = input("You: ")
	if msg == "exit":
		print("Bot: Bye!")
		break
	history.append("User: "+ msg)
	conv = "\n".join(history)
	response = client.models.generate_content(
		model="gemini-2.5-flash" ,
		contents=conv
	)
	print("Bot:", response.text)
	history.append("Bot: " + response.text)

