from google import genai

client = genai.Client(api_key="api key")

while True:
    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Gemini: Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=question
        )

        print("Gemini:", response.text)

    except Exception as e:
        print("Error:", e)s

