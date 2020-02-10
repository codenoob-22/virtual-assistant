import speech_recognition as sr
import assistant
# Making virtual assistant which uses voice input to perform specific tasks.


def Listen():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print("you said: " + command)
        except sr.UnknownValueError:
            command = Listen()
        return command


while True:
    command = Listen()
    lisa = assistant.Assistant()
    if "open subreddit" in command:
        lisa.subReddit(command)
    elif "open" in command:
        lisa.openWebsite(command)
    
    elif "stop listening" in command:
        s = 'okay bye bye!'
        print(s)
        break    
