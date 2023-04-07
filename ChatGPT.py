import openai_secret_manager
import openai

def ask_gpt(prompt):
    openai.api_key = secrets["api_key"]
    model_engine = "text-davinci-002"
    prompt = f"{prompt}\nAI: "
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

print("Welcome to ChatGPT!")
print("Type 'exit' or 'bye' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'bye']:
        print('AI: Goodbye!')
        break
    response = ask_gpt(user_input)
    print("AI:", response)
