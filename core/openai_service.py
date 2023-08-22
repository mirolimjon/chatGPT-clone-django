import openai

openai.api_key = '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'

def generate_text(message):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message },
        ]
    )
    print(response)
    print(response.choices[0].message.content.strip())
    answer = response.choices[0].message.content.strip()
    return answer