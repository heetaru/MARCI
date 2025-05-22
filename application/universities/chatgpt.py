import ast
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


# Ініціалізація клієнта з API ключем
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # 🔑 Встав свій ключ

# Діалогова функція
def chat_with_gpt(messages_history, user_input):
    if messages_history == "":
        messages = [
            {"role": "system", "content": "Ти дружній помічник, який відповідає українською."}
        ]
    else:
        messages = messages_history.copy()  # ✅ Вже список, просто копіюємо
        #messages = ast.literal_eval(messages_history).copy() #ця йобнута функіця потрібна шоб список привести в адекватний формат

    messages.append({"role": "user", "content": user_input})


    response = client.chat.completions.create(
        model="o4-mini-2025-04-16",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})
    return messages
