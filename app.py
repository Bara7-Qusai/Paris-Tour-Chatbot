
from openai import OpenAI

# إعداد النموذج والعميل
model = "gpt-4o-mini"
client = OpenAI(api_key="API_KEY_HERE")

# المحادثة الأساسية
conversation = [
    {"role": "system", "content": "You are a helpful Travel Guide providing concise info about Paris landmarks."},
    {"role": "assistant", "content": "The most famous landmark in Paris is the Eiffel Tower."},
    {"role": "user", "content": "What is the most famous landmark in Paris?"}
]

# قائمة الأسئلة
questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

# إرسال الأسئلة للنموذج والحصول على الردود
for q in questions:
    input_dict = {"role": "user", "content": q}
    conversation.append(input_dict)

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=150
    )

    resp = response.choices[0].message.content
    print(f"Q: {q}\nA: {resp}\n")

    response_dict = {"role": "assistant", "content": resp}
    conversation.append(response_dict)
