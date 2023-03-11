import openai

openai.organization = "org-Xt0Xx5e7hzi8j7eYV5nuk5k1"
openai.api_key = "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"
openai.Model.list()

def send_and_receive_msg(user_msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{user_msg}"}
        ]
    )

    # AI response
    ai_msg = response["choices"][0]["message"]["content"]
    return ai_msg




