import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


# Ініціалізація клієнта з API ключем
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # 🔑 Встав свій ключ

# Діалогова функція
def chat_with_gpt(message_history, user_input):
    if len(message_history) == 0:
        messages = [
            {"role": "system", "content": "Ти дружній помічник, який відповідає українською."}
        ]
    else:
        messages = [*message_history]

    user_input = user_input

    #messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="o4-mini-2025-04-16",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})
    return messages
