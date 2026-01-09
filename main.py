from idlelib.editor import darwin

import speech_recognition as sr
import win32com.client
import webbrowser
import os
import openai
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry, I didn't get that. Please try again."

if __name__ == '__main__':
    say("Hey! I am Kuko A I. How can I help you?")
    while True:
        print("Listening...")
        query = take_command()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://en.wikipedia.org"], ["github", "https://github.com/jkmloom"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        if "open music" in query:
            music_url = r"C:\Users\ROG\Downloads\pixel-dreams-259187.mp3"
            # opener = "open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, music_url])
            say("I found a music file in the system")
            os.startfile(music_url)

        if "the time" in query:
            strf_time = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {strf_time}")

        # if dev[0] in query or dev[1] in query:
        #     say("I was mainly developed by a small team of computer science students. Jatin Kumar Mehta, Aryan Shakya, and Abhishek Charak")

        # say(query)