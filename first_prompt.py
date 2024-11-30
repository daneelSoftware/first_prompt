import os
import datetime
import aisuite as ai
from gtts import gTTS

client = ai.Client()

models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]
messages = [
    {"role": "system", "content": "Respond in french."},
    {"role": "user", "content": "in what year was Soultzbach-les-bains first mentionned"},
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
    mytext = response.choices[0].message.content
    print(mytext)
    language = 'fr'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save('welcome.mp3')
    # read message with mediaplayer
    os.system('start welcome.mp3')

now = datetime.datetime.now()
print ('End of program at : ',now.strftime("%Y-%m-%d %H:%M:%S"))   

   
