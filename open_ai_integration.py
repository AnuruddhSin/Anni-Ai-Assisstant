import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "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"

lang = 'en'

openai.api_key = api_key

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

            if "Friday" in said:
                completion = openai.ChatCompletion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
                text = completion.choices[0].message.content
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.ui")
                speech.save("Well1.mp3")
                playsound.playsound("well1.mp3")

        except Exception as e:
            print(f"Exception: {e}")

    return said

while True:
    get_audio()
