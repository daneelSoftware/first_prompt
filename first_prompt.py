import os
import datetime
import aisuite as ai
client = ai.Client()

models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]
messages = [
    {"role": "system", "content": "Respond in German."},
    {"role": "user", "content": "in what year was Calmbach first mentionned"},
]
now = datetime.datetime.now()
print ('Begin of program at : ',now.strftime("%Y-%m-%d %H:%M:%S"))
print ('Models : ',models[0],models[1])

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)

#os.system('pause')
now = datetime.datetime.now()
print ('End of program at : ',now.strftime("%Y-%m-%d %H:%M:%S"))   